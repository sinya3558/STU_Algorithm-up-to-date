# 음료수 얼려 먹기
'''
- 첫 번째 줄 얼음 틀의 세로 N, 가로 M ( 1 <= N, M <= 1000), N(row) M(col)
- 두 번째 줄부터 N+1 번째 줄까지 얼음틀의 형태 주어짐
- 얼릴 수 있는 부분 : 0
- 얼릴 수 없는 부분 : 1
일때, 한 번에 만들 수 있는 아이스크림의 개수를 출력하시오

input
4 5
00110
00011
11111
00000

output
3
'''
# DFS 사용하면 안되려나
'''
- 위 아래 오 왼 체크 -> 0 이고 방문한적 없으면 = 방문해
- 반복해서 연결된 얼음틀 모두 체크
- 방문안한 지점 카운트
'''
# user input
N, M = map(int, input().split())

# 2d list user input : 얼음틀 받기
ice_tool = []
for i in range(N):  # 아 M 받아서 하다가 망했.. 바보야 row, colum 적어두고 시작해
    ice_tool.append(list(map(int, input())))

# dfs
def dfs(row, col):
    # 네모네모 칸 만들기
    if (row <= -1 or row >= N) or (col <= -1 or col >= M) :
        return False
    # 0,0 부터 visted 여부 체크
    if ice_tool[row][col] == 0:
        # mark curr node visited
        ice_tool[row][col] = 1
        # 위 아래 왼 오 위치 재귀적으로 호출
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col -1)
        dfs(row, col + 1)
        return True
    return False

# 받은 위치 참고해서 음료수 채우기
cnt_icecream = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            cnt_icecream += 1
print(cnt_icecream)