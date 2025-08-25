#01:03:09.25
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

'''
코드 참고 : https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94

인접한 배추끼리 배추흰지렁이 하나씩 => 필요한 배추흰지렁이 갯수 세는 문제
- 인접한 배추를 탐색하기 위해 BFS.
- 배추밭을 표현하기 위해 cabbage_field 2차원리스트 선언해서 배추있는 곳은 1, 아닌 곳은 0으로
- 1,0 => cabbeage_field[0][1]로 x가 열(가로길이 < M), y가 행(세로 길이 < N)
- BFS로 방문한 배추는 그냥 cabbage_field[y][x] = 0 으로 방문 처리.
- 인접하지 않은 떨어져 있는 배추 그룹이 있을 수 있으므로, cabbage_field[i][j] == 1인 곳(배추) 또 찾아서
    BFS함수 호출
'''

def BFS(y, x, M, N, cabbage_field):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(y, x)])
    # 방문 처리로 배추 있는 곳을 0으로 바꿈.(인접하지 않은 다른 배추그룹 찾을 떄 사용하려고)
    cabbage_field[y][x] = 0
    
    while queue:   
        cy, cx = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            # M은 가로(열), N은 세로(행)이므로
            # 0<= ny < N은 세로 범위, 0<= nx < M은 가로 범위
            if 0 <= ny < N and 0 <= nx < M:
            #if nx < 0 or nx >= M or ny < 0 or ny >= N:
            #    continue
                # 현재 인접한 배추 있으면
                if cabbage_field[ny][nx] == 1:
                    # 해당 배추 위치 큐에 넣어 여기서 또 인접한 배추 탐색할 수 있도록
                    queue.append((ny, nx))
                    cabbage_field[ny][nx] = 0 # 방문 처리
    
T = int(input().strip())

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage_field = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage_field[Y][X] = 1 # (Y,X) 위치에 배추 있음.
    
    cnt_worm = 0 # 배추흰지렁이 갯수를 셀 변수
    # 배추가 있으면 BFS를 통해 연결된 배추 모두 방문하기 위해 배추밭을 전체 순회
    for i in range(N):
        for j in range(M):
            # 배추 있으면
            if cabbage_field[i][j] == 1:
                # 인접한 모든 배추 방문
                BFS(i, j, M, N, cabbage_field)
                # 하나의 덩어리 끝났으므로 지렁이 한마리 추가.
                cnt_worm += 1
                
    print(cnt_worm)