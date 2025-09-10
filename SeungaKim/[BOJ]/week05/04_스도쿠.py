# https://www.acmicpc.net/problem/2239 
# Q. 인풋 데이터 저장해두고 따로 불러오는거 필요해... 
import sys
# get user input
ROW = 9 
COL = 9
# init 9x9 sudoku board
# sudoku= [[] * COL for _ in range(ROW)]
sudoku= [[0] * COL for _ in range(ROW)] # 똑같은 실수를 또 반복하고

# sudoku:list[list[int]] = []
# with open("input.txt","r") as f:
#     for f_ele in f.readlines():
#         sudoku.append(f_ele.strip())


# assign user input to the sudoku board
for r in range(ROW):
    user_input_by_row = sys.stdin.readline().strip()  # divide by '\n' -> mem eff
    sudoku[r] = list(map(int, user_input_by_row))   # convert str -> list(int)

# find 0's and save that position(r,c) to list
# zero_list = []
# for r in range(ROW):
#     for c in range(COL):
#         if sudoku[r][c] == 0:
#             zero_list.append((r, c))    # tuple bc position never change
# # print(zero_list)

# nested loop 시간 아껴
zero_list = [(r, c) for r in range(ROW) for c in range(COL) if sudoku[r][c] == 0] 
# print(f'ZERO LIST VALS: ', zero_list)
'''
Backtrace?
- 일단 dfs & recursive call
- if satisfies condition -> pass, otherwise -> backtrace(back to prev step)

for this sudoku, condition is equal to 
1. have you found val in the matrix?
    if yes, pass and recursive call
    otherwise, go back to prev step which is 0
'''
# 1 ~ 9 에서 임의의 수 넣어서 알맞은 자리인가 확인하고 싶어
def check_value(new_val, board, r, c):
    '''
    param
        new_val = 우리가 넣고자 하는 값 1 ~ 9
        board = sudoku board, r = ROW, c = column
    rt_val
        boolean
    '''
    # 1. check COL 0 to 8 corresponding to 'r' position. If value exists,
    if new_val in board[r]:
        return False
    # 2. check ROW 0 to 8 corr to 'c'
    for r_idx in range(9):
        if board[r_idx][c] == new_val:
            return False
    # 3. check 3x3 sudoku area
    mini_r_s= (r//3) * 3   # starts at 0 or 3 or 6
    mini_c_s = (c//3) * 3 
    for rb in range(3):
        for cb in range(3):
            # set up 3x3 area from starting points of mini ROW and mini COL
            if board[mini_r_s + rb][mini_c_s + cb] == new_val:
                return False
            
    # otherwise, pass all the condition
    # assign new_val instead of 0
    return True

def dfs_backtrace(zero_pos):    # 아니! 왜 zero list 안 넣어? 왜! else 있으면 값 업데이트 안되??
    '''
    - zero_pos = (r,c) of 0's from the zero_list
    - zero_list
    - no return value = only update vals in sudoku
    '''

    '''
    things to do 
        1. zero pos 끝날 때 까지
            1-1 zero_pos(r, c) 받기 -> Q. 이거 dfs_backtrace 밖에서 해도 괜찮은가?
            1-2 board[r][c] 알맞으 ㄴ값 넣을 수 있나 체크
                1-2-1 pass? 
                    - b[r][c] = new_val
                    - dfs(next zero)
                1-2-2 backtrace
                    - to b[r][c] = 0
    '''
    # stop condition for recursive call
    if zero_pos == len(zero_list):
        return True # Q. 이거 맞나 그냥 함수에서 나가는 거 없나?
    # 1-1
    # r_zero, c_zero = map(int, zero_list[zero_pos])  # Q. 여기서 자꾸 에러남! 괜히 튜플로 했나?
    r_zero, c_zero =zero_list[zero_pos]
    # 1-2. (1 ~ 9) 사이에 알맞은 값 찾기
    for random_val in range(1, 10):
        if check_value(random_val, sudoku, r_zero, c_zero):
            # 1-2-1. if pass condition, call recursive fun with next 0
            # 아 이거 까먹음, update value -> Q. 왜 업데이트가 안되지?
            sudoku[r_zero][c_zero] = random_val
            # dfs_backtrace(zero_pos + 1)
            if dfs_backtrace(zero_pos + 1):
                # ****************** 에헤이 멍충아 스도쿠 업데이트 하고 끝내야지
                return True
        # 1-2-2. if fail to pass, return to prev value
        # else:
        sudoku[r_zero][c_zero] = 0  
    return False

# print('--output--')
# function calls & print final output
dfs_backtrace(0)    # 0인 원소들의 리스트 전부 체크
for r in sudoku:
    # print(sudoku[r])
    print(''.join(map(str,r)))   # 스도쿠 값들 한줄씩 빈칸 없이 붙여서 출력하기

