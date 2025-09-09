#01:52:54.12
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()
'''
각각의 보드의 블록의 위치와 블록을 놓는 방향성을 고려하여 점수계산하고 남아있는 타일 세는 문제
- 매 턴마다 초록보드(위 -> 아래)와 파랑보드(왼 -> 오)로 블록이 떨어지고 난 뒤, 행이나 열에 블록이
    꽉차있으면 없애고 옮기고, 연한영역도 따로 처리해주니까 시뮬레이션
1. 블록 놓기
    - 행 또는 열을 순회하며 빈칸을 찾아야하기 때문에 while문으로 돌면서 빈 칸에 최종블록을 놓음
2. 꽉 찬 행/열 처리
    - 보드를 한 줄씩 체크하기 위해 all()로 접근
    - 꽉 찼다면 지우고 score+= 1, 그리고 지운 줄에 블록 이동시켜야하기 때문에 del해버리고 맨 앞이나 왼쪽에 새로운 행/열 insert
3. 0,1 행/열 처리
    - 0,1 행/열에 있는 블록 세기 위해 any()로 접근해서 행/열 갯수 셈
    - 갯수 만큼 지우고 이동시켜야하기 때문에 맨 아래/오른쪽 줄을 del하고 맨앞/왼쪽에 새로운 행/열 insert 
4. 마지막 타일 갯수 세기
'''

blue_board = [[0] * 6 for i in range(4)]
green_board = [[0] * 4 for i in range(6)]

score = 0

def drop_green(t, x, y):
    if t == 1: # 1*1
        r = 0
        while r < 6 and green_board[r][y] == 0:
            r += 1
        green_board[r-1][y] = 1
        
    elif t == 2: # 1*2
        r = 0
        while r < 6 and green_board[r][y] == 0 and green_board[r][y+1] == 0:
            r += 1
        green_board[r-1][y] = green_board[r-1][y+1] = 1
        
    else: # t == 3, 2*1
        bot_r = 1 # 위아래 블록 중 아래블록
        while bot_r < 6 and green_board[bot_r][y] == 0:
            bot_r += 1
        green_board[bot_r - 2][y] = green_board[bot_r - 1][y] = 1

def clear_full_rows_green(): # 꽉찬 행이 있으면 없애기
    global score
    r = 2 # 0,1행 확인할 필요없음
    while r < 6:
        if all(green_board[r][c] for c in range(4)):
            score += 1
            del green_board[r] # 줄 삭제 -> 알아서 내려옴
            green_board.insert(0, [0] * 4) # 맨 위에 빈 줄 삽입
        else:
            r += 1
            
def handle_light_green(): # 0,1행이 차 있는 행수만큼 맨 아래행 지우기
    kill_r = 0
    # 0,1행 중 블록있는 부분 찾기
    for r in [0, 1]:
        if any(green_board[r][c] for c in range(4)):
            kill_r += 1
    # 블록 있는 부분 지우고 밑에 빈 행 삽입
    for _ in range(kill_r):
        del green_board[-1]
        green_board.insert(0, [0] * 4)
    
def drop_blue(t, x, y):
    if t == 1: # 1*1
        c = 0
        while c < 6 and blue_board[x][c] == 0:
            c += 1
        blue_board[x][c-1] = 1
        
    elif t == 2: # 1*2
        right_c = 1 #왼쪽 오른쪽블록 중 오른쪽 블록
        while right_c < 6 and blue_board[x][right_c] == 0:
            right_c += 1
        blue_board[x][right_c - 2] = blue_board[x][right_c-1] = 1 
        
    else: # t == 3, 2*1
        c = 0
        while c < 6 and blue_board[x][c] == 0 and blue_board[x+1][c] == 0:
            c += 1
        blue_board[x][c-1] = blue_board[x+1][c-1] = 1
        
def clear_full_cols_blue():
    global score
    c = 2 # 2열부터
    while c < 6:
        if all(blue_board[r][c] for r in range(4)):
            score += 1
            for r in range(4): # 모든 행에서 c열 제거하고 왼쪽에 빈 열 삽입
                blue_board[r].pop(c)
                blue_board[r].insert(0, 0)
        else:
            c += 1
    
def handle_light_blue():
    # 0, 1열 중 블록 있는 열 수
    kill_c = 0
    for c in [0, 1]:
        if any(blue_board[r][c] for r in range(4)):
            kill_c += 1
    # 맨 오른쪽 열을 kill_c만큼 지우고 그만큼 왼쪾에 빈 열 추가
    for _ in range(kill_c):
        for r in range(4):
            blue_board[r].pop()
            blue_board[r].insert(0, 0)

def cnt_tiles():
    sum_tiles = 0
    for r in green_board:
        sum_tiles += sum(r)
    for r in blue_board:
        sum_tiles += sum(r)
        
    return sum_tiles

N = int(input())
for _ in range(N):
    t, x, y = list(map(int, input().split()))
    
    # 초록 보드 처리
    drop_green(t, x, y)
    clear_full_rows_green()
    handle_light_green()
    
    # 파랑 보드 처리
    drop_blue(t, x, y)
    clear_full_cols_blue()
    handle_light_blue()

print(score)
print(cnt_tiles())