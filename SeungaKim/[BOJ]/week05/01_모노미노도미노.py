# https://www.acmicpc.net/problem/20061
# 10:35
# 아이디어
'''
일단 
보드
    1. 보드 셋업, 
        red =   x(0:3) * y(0:3)
        blue =  x(0:3) * y(4:9)     -> light zone = y[4:5]
        green = x(4:9) * y(0:3)     -> light zone = x[4:5]
블럭 두기 & 삭제    
    2. 왠지 dfs 일 것 같음 visited true 면 그 위의 행 or 왼쪽렬에 블럭 쌓고, 아니면 각 행 렬 끝까지 이동시키고
    ###### 아니 bfs 인가.. queue에다가 (x,y) 넣어서 다 뺼때까지 돌리는?
    ###### dfs 랑 bfs 구분이 잘 안됨..
    3. green y[0:3] 가득차면, 그 렬 pop & blue x[0:3] 가득ㅏ면 그 행 삭제
    4. 3번 이후에 점수 + (삭제된 횟수만큼)
이동
    5. 행 또는 렬 삭제 이후에 이전에 존재하는 블럭들 아래 또는 오른쪽으로 전체 이동
    6. 그리고 각 구간의 light zone 에 존재하는 블럭에 따라서 1~2칸씩 전체 삭제
    7. 삭제된 만큼 아래 또는 오른쪽으로 블럭 전체 이동 -> 점수 추가 x
특수 케이스
    8. (light zone 에 블럭 존재해서 삭제) && (green y[0:3] & blue x[0:3] 가득차서 삭제) -> 이 경우 점수추가가 먼저 + 이동, 그 후에 연한 칸 삭제 적용
결과 프린트
    - 토탈 점수
    - sum(그린, 블루 남아있는 블럭의 개수)
'''
#10:45
#19:48
import sys
from collections import deque
# get user input
N = int(input())
if not 1 <= N <= 10000:
    sys.exit()

while N:
    T, X, Y = map(int, input().split())
    N -= 1
'''
# 1. Set up the board
common_r = 4
common_c = 4
# init RGB boards
domino_b = [[] for _ in range(common_r) for _ in range(common_c +  6)]
domino_g = [[] for _ in range(common_r + 6) for _ in range(common_c)]
domino_r = domino_b[0:4][0:4] or domino_g[0:4][0:4] # 요기 야매임
# light zones
light_B = domino_b[0:4][4:6]
light_G = domino_g[4:6][0:4]

# Set up type of moving blocks
BLOCK_TYPE = [(0,0), (1, 1), (1, 2), (2, 1)]   # 0 = 임의의 수(type idx 맞추려고 추가함) / 1 = 1x1 / 2 = 1x2 / 2 = 2x1
direct_x = [0, 1, 0]            # 맞는지 모르겟다
direct_y = [0, 0, 1]            # 얘도
'''
# 모르겠음 할 수 있는 것 부터

# Set up board
COMMON_R = 4
COMMON_C = 4
# RGB boards
board_r = [[] for _ in range(COMMON_R) for _ in range(COMMON_C)]
board_b = [[] * (COMMON_C + 6) for _ in range(COMMON_R)]
board_g = [[] * COMMON_C for _ in range(COMMON_R + 6)]
# light boards
light_b = board_b[0:COMMON_R][4:6]
light_g = board_g[4:6][0:COMMON_C]

# for r in 

# Q. 그래프 bfs 에 넣어줘야될텐ㄷ디. 아니면 그냥 10x10 board 로 시작하나? 메모리 너무 잡아먹지 않나?
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
# 9:49

# 집가서,
'''
    1. bfs 쓰는 법 정확히 알기
    2. 명진님 설명 들어서 이해할 정도는 되어야 할 것 아니야
    3. 내 문제도 왜 스도쿠 값이 업데이트 안되는지 찾아보기 
'''
board = [[] * range(10) for _ in range(10)]
print(board)