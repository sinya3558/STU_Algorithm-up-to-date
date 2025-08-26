#01:00:18.62
import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
인접한 나라끼리의 인구 차이를 조건으로 두고 조건에 맞으면 계속해서 인구를 이동시키는 문제
- 인접한 나라를 조건에 따라서 연합으로 묶어서 이동할 인구를 계산해야하므로 BFS로 탐색
1. 하루동안 BFS로 조건에 맞는 모든 연합을 탐색
    - 찾은 연합에 속하는 나라들의 좌표를 저장하기 위해 union 변수 선언
    - 연합의 총 인구 수를 계산하기 위해 total_p 변수 선언
    - 인접한 두 나라의 인구 차이를 조건으로 더해 조건에 맞으면 연합이므로
        큐에 넣고, 방문 표시하고, 좌표추가하고 인구수 더함
    - 끝나면 연합에 속하는 나라와 총 인구수를 BFS 밖에서 계산하기 위해 반환
    
2. 탐색된 연합의 인구를 재분배하고 더 이상 이동이 없을 때까지 반복
    - 인구 이동이 발생한 날짜 수를 저장하기 위해 result 변수 선언
    - visited 배열은 매일 새로운 BFS를 시작해야하므로 초기화 하고 bfs함수에 인자로 넘겨줌
    - 인구이동 여부를 저장하기 위해 moved 변수 선언
    - 0,0에서 BFS 시작하고 len(union)이 1이면 연합없으니까 인구이동 없고 >1 이면 인구이동
    - 새로운 인구수 계산해 new_pop애 저장해 인구 재분배
    - 인구이동이 없었다면 break로 종료, 있었다면 result += 1
'''

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    union = [(x, y)]
    total_p = country[x][y]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(country[cx][cy] - country[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_p += country[nx][ny]
    return union, total_p

result = 0
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False # 인구 이동 할지말지
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, total_p = bfs(i, j, visited)
                if len(union) > 1:
                    moved = True
                    new_p = total_p // len(union)
                    for ux, uy in union:
                        country[ux][uy] = new_p
    if not moved:
        break
    result += 1
print(result)
                  
                
            
    