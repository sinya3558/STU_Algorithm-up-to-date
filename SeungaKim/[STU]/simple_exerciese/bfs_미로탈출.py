# 미로탈출!
'''
- 첫 째줄에 N, M (4 <= N, M <= 200)
- 0 (괴물 있음. 피해!)
- 1 (괴물 없음. 통로)
- 이동은 한 칸씩 할 때, 최소 이동 칸의 개수를 출력하라

input
5 6
101010
111111
000001
111111
111111

output 10
'''
# N(row) x M(col)
# User input : 미로 사이즈
N, M = map(int, input().split())

# User input : 미로 구성
maze = []
for x in range(N):
    maze.append(list(map(int, input())))
# print(maze)

# 아.... 길찾기. 최단거리 찾기! -> bfs
# 가까운 노드부터 탐색 (첫 노드와 거리 차이 1!!!!)

# 값이 1인 노드 and 미방문 노드 -> queue 에다가 (1)삽입하고 (2)방문찍고 (3) 이전 최단거리 + 1 : 카운트 하고

# 이동할 방향 정의(위, 아래, 왼, 오)
direct_x = [-1, 1, 0, 0]
direct_y = [0, 0, -1, 1]

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))  # 오호..왜 (()) 더블이야? 2d 라서?
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 위 아래 왼 오 4 가지 방향으로 위치 확인
        for i in range(4):
            new_x = x + direct_x[i] # 다음 인접 노드(상하)
            new_y = y + direct_y[i] # 다음 인접 노드 (좌우)
            # 미로 범위 벗어난 경우 -> 무시
            if (new_x < 0 or new_x >= N) or (new_y < 0 or new_y >= M):
                continue
            # 괴물 있는 경우 -> 무시
            if maze[new_x][new_y] == 0:
                continue
            # 그 외 경우, 미방문인 경우에만 최단 거리 기록 
            if maze[new_x][new_y] == 1:
                maze[new_x][new_y] = maze[x][y] + 1     #  이걸 잘 모르겠어. 아 카운트 대신 이전값 +1
                q.append((new_x, new_y))

    return maze[N-1][M-1]   # 리턴으로 q 하려했는데.. 아님

print(bfs(0,0))

