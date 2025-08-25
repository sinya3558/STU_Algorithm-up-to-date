#00:55:00:00
import sys
from collections import deque

#sys.stdin = open("input.txt",'r')

'''
코드 참고 : https://velog.io/@seungjae/%EB%B0%B1%EC%A4%80-2178%EB%B2%88-%EB%AF%B8%EB%A1%9C%ED%83%90%EC%83%89-Python-BFS"

시작점에서 넓게 탐색해야하기 때문에 BFS 문제이므로 deque를 이용해 구현
미로에서 이동하려면,
 - 통로(0 아니고 1)임을 확인해야 해서 현재 위치의 상하좌우 확인 필요
 - 방문하지 않은 칸임을 확인해야 해서 방문한 칸을 저장하는 visited 배열 선언
N, M까지의 최단거리 구해야 해서 시작점부터 각 칸의 위치까지의 거리 저장하는 distance 배열 선언
'''

N, M = list(map(int, sys.stdin.readline().strip().split()))

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))
#maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[False for _ in range(M)] for i in range(N)]
# 시작점을 포함한 거리니까 1로 초기화
distance = [[1 for _ in range(M)] for i in range(N)]

# 좌(0,-1), 우(0,1), 하(-1,0) 상(+1, 0)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0,0)) # 시작 위치
    while queue:
        x,y = queue.popleft()
        #현 위치의 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위 벗어나지 않으면
            if 0 <= nx < N and 0<= ny < M: 
                # 방문하지 않았고, 통로라면 방문
                if not visited[nx][ny] and maze[nx][ny] == 1: 
                    # 큐에 추가하고 방문 처리 
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    # 거리 갱신 (현재 칸까지의 거리 +1)
                    distance[nx][ny] += distance[x][y] 
bfs()
print(distance[N-1][M-1])           