# https://www.acmicpc.net/problem/16234

# 1. 문제 설명
'''
- NxN 크기의 땅(1x1사이즈로 이루어진)
- 각각의 땅에는 나라가 하나씩 존재하며 r행 c열에 존재하는 나라의 인구는 A[r][c]명
- 인접한 나라 사이에는 정사각형 형태의 국경선 존재
- 인구 이동 작동 원리
--- 국경선 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 국경선을 하루 동안 연다
--- 국경선이 열리면 인구 이동 시작한다. 인접한 칸만 이동가능하며, 두 나라를 하루 동안 연합이라고 부른다. 
--- 연합을 이루는 각 칸의 인구수는 (연합의 인구수)/(연합을 이루는 칸의 개수)
--- 연결 해체 -> 국경선 닫는다. 인구 이동이 며칠 동안 발생하는지 구하라
'''
# 2. 문제 해결 아이디어
'''
BFS는 최단거리 찾기니까 DFS로 recursive?
인구 차이 계산은 어떤식으로 하지..?
마지막에 사람 수 재분배 : (사람수 총합)/(나라 개수 총합)
'''
# 3. 몰랐던 것 (참고 부분)
'''
[인구차이 계산]
- abs(map[row][col] - map[n_row][n_col])

[탐색 방향]
상하좌우 네 방향 전부 탐색
- for i in range(4)   # direction row, col 이 [0, 0, 0, 0] 바탕이라서
만약 대각선 이동까지 전부 탐색한다면?
- for i in range(8)     # direct_r, c = [1, -1, 0, 0, 1, 1, -1, -1] 여덟개 방향으로 이동 가능
'''
# 4. 소스 코드
# 09:49
import sys

# user input : N L R
N, L, R = map(int, input().split())
if not (1 <= N <= 50) or not (1 <= L <= R <= 100):
    sys.exit

# user input : population
land_map = []
for _ in range(N):
    land_map.append(list(map(int, input().split())))    # 그냥 assign 아니고 append() 써야지 리스튼데 이 바보야
# print(land_map)

# def count_movements_of_population(n, l, r, map):
#     '''
#     parameter
#         n = size of matrix (int)
#         l = min nums of population to migrate(int)
#         r = max " (int)
#         map = 2d NxN list

#     rt_val
#         cnt = counts of movement(int)
#     '''
#     cnt = 0
#     diff = 0

#     # check boundaries
#     for row in range(n):
#         for col in range(n):
#             # print(map[row][col])
#             if (row < 0 or row >= N) or (col < 0 or col >= N):
#                 return False
#             diff = abs(map[row][col])
#             # 11:15 ( 1h 35m)
#             # 12:44
#             if l <= map[row][col] <= r:

#     return cnt

# print(count_movements_of_population(N, L, R, land_map))

# 좌표 이동 위치 declare
direct_row = [-1, 1, 0, 0]      # up, down
direct_col = [0, 0, -1, 1]      # left, right

# dfs -> recursive func( 필요한 parameters 구분할 것)
def search_dfs(n, l, r, map, row, col, visited, country):
    # first visit
    visited[row][col] = True    # visted 를 여기서 init 하는구나. 밖에서 하는줄
    country.append((row, col))

    for i in range(4):
        n_row = row + direct_row[i] # 위 아래 체크
        n_col = col + direct_col[i] # 왼 오 체크
        # 체크 바운더리
        if (n_row < 0 or n_row >= n) or (n_col < 0 or n_col >= N) and visited[n_row][n_col]:
            return False    # 이게 맞나
        else :
            diff = abs(map[row][col] - map[n_row][n_col])
            if l <= diff <= r :
                search_dfs(n, l, r, map, n_row, n_col, visited, country)


def count_movements(n, l, r, map):
    cnt = 0
    while True:
        # 처음 모든 노드 not visited 초기화
        visited = [[False] * n for _ in range(n)]      # [[False] * n * n] 안됨!!!!!
        # 그 뭐냐 그..barrier? border 체크
        open_border = False     # is closed

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:   # map[i][j] 랑 visited 비교하는거 아냐!!
                    merged_country = []
                    search_dfs(n, l, r, map, i, j, visited, merged_country)

                    # 매트릭스 다 확인했다는 가정하에, 마지막으로 인구수 재분배
                    if len(merged_country) > 1: # 연합이 1개 이상이면,
                        open_border = True      # border 열고
                        # 사람수 새롭게 분배
                        total_pop = sum(map[row][col] for row, col in merged_country)
                        new_pop = total_pop // len(merged_country)
                        # 새로운 인구수 계산 끝 -> assign
                        for row, col in merged_country:
                            map[row][col] = new_pop

        if not open_border:
            break
        cnt += 1
    return cnt

print(count_movements(N, L, R, land_map))
# 1h35m + 1h06m = 2h41m