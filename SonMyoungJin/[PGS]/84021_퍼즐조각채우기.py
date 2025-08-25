#02:00:00.00
from collections import deque

'''
코드 참고: https://eunbin00.tistory.com/190

1. BFS로 빈블럭과 퍼즐 조각을 찾음
2. 퍼즐조각을 회전시켜서 빈블럭에 들어가는지 확인해야 하기 위해 bfs_blocks 함수 정의
    - 찾은 퍼즐조각 인덱스로 2차원 배열만들기 위해 block_2d 함수 정의
    - 만든 퍼즐조각 2차원 배열을 돌리기 위해 rotate 함수 정의
'''

# 빈 블럭이나 퍼즐 조각을 BFS로 찾는 함수
def bfs_blocks(graph, flag):
    N = len(graph)
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(N)]
    blocks = []
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == flag and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                graph[i][j] = flag ^ 1 # 1^1 = 0, 0^1 = 1
                block = [(i, j)]
                
                while queue:
                    cx, cy = queue.popleft()
                    for k in range(4):
                        nx, ny = cx + dx[k], cy + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if graph[nx][ny] == flag:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                graph[nx][ny] = flag ^ 1 # 1^1 = 0, 0^1 = 1
                                block.append((nx, ny))
                blocks.append(block)

    return blocks

# 빈 블럭이나 조각 인덱스를 받아서 2차원 배열로 만들어주는 함수
def block_2d(block):
    x, y = zip(*block)
    col, row = max(x) - min(x) + 1, max(y) - min(y) + 1
    arr = [[0] * row for _ in range(col)]
    
    for i, j in block:
        i -= min(x)
        j -= min(y)
        arr[i][j] = 1
        
    return arr

# 오른쪽으로 90도씩 회전
def rotate(piece):
    rotate = [[0] * len(piece) for _ in range(len(piece[0]))]
    cnt = 0
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                cnt += 1 # 면적계산하기위해
            rotate[j][len(piece) - 1 - i] = piece[i][j]
    return rotate, cnt
        

def solution(game_board, table):
    answer = 0
    pieces = bfs_blocks(table, 1)
    empty_blocks = bfs_blocks(game_board, 0)
    
    for empty_block in empty_blocks:
        filled = False # 현재 빈공간
        empty_2d = block_2d(empty_block)
        for piece in pieces:
            if filled == True: # 이미 채워져있으면 다음 공간으로
                break
            piece_2d = block_2d(piece)
            for i in range(4):
                piece_2d, cnt = rotate(piece_2d)
                if empty_2d == piece_2d:
                    answer += cnt
                    pieces.remove(piece)
                    filled = True # 빈 공간 채워짐
                    break
    
    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
'''
game_board = [[0,0,0],[1,1,0],[1,1,1]]
table = [[1,1,1],[1,0,0],[0,0,0]]	
'''
print(solution(game_board, table))