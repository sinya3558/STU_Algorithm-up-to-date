#1:55:29:28
import sys
from collections import deque

#sys.stdin = open("input.txt", 'r')
'''
에어컨에서 나오는 바람이 물건에 의해 방향바꾸면서 연구실에 퍼져나가는데, 퍼져나가는 부분 계산하는 문제
- 에어컨 여러개 있을 수 있음
- 각 물건은 바람 방향 변경하거나 특정 방향으로 갈 수 있도록 제한
- 바람 닿은 자리 count

    처음에는 에어컨에서 시작해 바람이 물건에 닿을 때까지를 모두 세기 위해 DFS로 구현하고자 함.
    - 물건에 닿았을 때마다 DFS를 재귀호출하면 모든 방향에 대해서 물건 닿을 때마다 재귀호출해야하므로 복잡, 비효율적
    => 그래서, 에어컨 바람은 4방향으로 퍼지니까 넓게 접근해야 한다는 아이디어 가지고 BFS로 다시 구현
    - BFS는 각 칸을 한번만 방문하므로 한번 탐색으로 모든 방향의 바람 경로를 추적하는 것이 가능

1. 에어컨 위치 찾고 큐에 삽입
- 바람의 시작점은 에어컨의 위치이므로 연구실 구조를 lab에 저장하고 에어컨 위치(9)인 곳 찾음
- BFS로 사용하기 위해 deque()사용하여 queue 정의하고 queue에 에어컨 위치 append
    - 에어컨은 여러 개일 수 있기 때문에, BFS를 시작해야되는 모든 지점을 append
    - 민상이가 앉을 수 있는 자리를 기록할 seat배열 0으로 초기화, 에어컨 위치는 앉을 수 있으니까 1

2. 바람의 확산
- 바람이 이동할 새로운 좌표 계산 하기 위해 dx, dy로 상하좌우를 정의함
    - 에어컨 위치 + (상,하,좌,우) = row, col
    
- 바람의 새로운 좌표에 물건 있으면, 바람의 방향은 바뀜 => if문으로 물건 있는지 검사해줌
    - 상하좌우를 물건에 따라 바꾸어서 이동값 nx, ny를 업데이트
    
    예)물건3  상(-1,0) => 우(0, 1)
            하(1,0) => 좌(0, -1)
            => 부호와 위치 바꿔주면 됨
            nx, ny = -ny, -nx
            
    예)물건1 상하는 보내주고, 좌우는 차단
            nx == 0 이면 좌우로 퍼지는 바람이므로 차단하기 위해 break

    - 연구실 범위 안까지 해당 좌표에 물건이 없다면 그대로 업데이트하여 바람 퍼트리기 위해
        - row += nx, col += ny 업데이트
        - while문으로 row, col이 범위 안이면 계속 돌도록
        
    - 연구실의 범위 안까지 바뀐 방향에 따른 바람의 이동값을 업데이트하여 바람을 퍼트리기 위해
        - row += nx, col += ny 업데이트
        - while문으로 row, col이 범위 안이면 계속 돌도록
'''
N, M = map(int, sys.stdin.readline().strip().split())

lab = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
seat = [[0] * M for _ in range(N)]
queue = deque()

# N*M 배열에서 움직임 => 상(-1,0) 하(1,0) 좌(0,-1) 우(0,1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#에어컨 위치 찾기, 큐에 위치 넣고, 앉을 수 있으니까 seat 배열에 1로 표시
for i in range(N):
    for j in range(M):
        if lab[i][j] == 9:
            queue.append((i, j))
            seat[i][j] = 1         

def BFS(lab, queue):
    # 큐가 빌 때까지 => 에어컨 수 만큼 BFS함
    while queue:
        x, y = queue.popleft() # 현재 에어컨 위치 꺼냄
        for i in range(4):
            nx, ny = dx[i], dy[i] # 현재 방향에 대한 이동 값 nx, ny에 저장
            row, col = x + nx, y + ny # 바람이 이동할 새로운 좌표
            
            # 연구실 범위 벗어나지 않으면 계속 퍼뜨림
            while 0 <= row < N and 0 <= col < M:
                seat[row][col] = 1 # 바람 닿으면 방문
                
                if lab[row][col] == 9: # 에어컨을 만나면 중단
                    break
                
                # 물건 3은 상(-1,0)->우(0,1), 하(1,0)->좌(0, -1)로 방향 바꿈
                if lab[row][col] == 3:
                    nx, ny = -ny, -nx
                # 물건 4는 상(-1,0)->좌(0,-1)으로 방향 바꿈
                elif lab[row][col] == 4:
                    nx, ny = ny, nx
                # 물건 1은 상하만 퍼지게 => 좌우 퍼지는 경우는 멈춤
                # 물건 2는 좌우만 퍼지게 => 상하 퍼지는 경우는 멈춤  
                elif (lab[row][col] == 1 and nx == 0) or (lab[row][col] == 2 and ny == 0):
                    break
                # 바람이 물건을 마주치고 나서의 바뀐 방향을 적용해(이동값 더해) 바람을 계속 퍼트림 
                row += nx
                col += ny
    result = 0
    for se in seat:
        for s in se:
            result += s
    
    return result
           
print(BFS(lab, queue))
    

'''
DFS 실패

def DFS(row, col, lab, stack)
    if 0 <= row <= N and 0 <= col <= M:
            if (row, col) not in stack and lab[row][col] == 0:
                stack.append((row, col))
                print(stack)
                seat += 1
                DFS(row - 1, col, lab, stack)
                DFS(row + 1, col, lab, stack)
                DFS(row, col - 1, lab, stack)
                DFS(row, col + 1, lab, stack)
            elif lab[row][col] == 9:
                stack.append((row, col))
                print(stack)
            else: # 숫자라면
                p_row, p_col = stack.pop()
                stack.append((row, col))
                seat += 1
                if lab[row][col] == 1:
                    if p_col > col: #상
                        DFS(row, col - 1, lab, stack)
                    elif p_col < col: # 하
                        DFS(row, col + 1, lab, stack)
                    # 좌우 방향 => 현재 위치(row, col) 까지   
                elif lab[row][col] == 2:
                    if p_row > row: #좌
                        DFS(row - 1, col, lab, stack)
                    elif p_col < col: # 우
                        DFS(row + 1, col, lab, stack)
                    # 상하 방향 => 현재 위치(row, col) 까지
                elif lab[row][col] == 3:
                    if p_col > col: #상
                        DFS(row + 1, col, lab, stack)
                    elif p_col < col: # 하
                        DFS(row - 1, col, lab, stack)
                    elif p_row > row: # 좌
                        DFS(row, col + 1, lab, stack)
                    elif p_row < row: # 우
                        DFS(row, col - 1, lab, stack)
                else: #4
                    if p_col > col: #상
                        DFS(row - 1, col, lab, stack)
                    elif p_col < col: # 하
                        DFS(row + 1, col, lab, stack)
                    elif p_row > row: # 좌
                        DFS(row, col - 1, lab, stack)
                    elif p_row < row: # 우
                        DFS(row, col + 1, lab, stack)
DFS(air[0], air[1], lab, stack)
'''