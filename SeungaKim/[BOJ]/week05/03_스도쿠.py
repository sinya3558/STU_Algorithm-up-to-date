# https://www.acmicpc.net/problem/2239 
import sys
# 주석처리 삭제 버전
ROW = 9 
COL = 9
sudoku = [[0] * COL for _ in range(ROW)]
for r in range(ROW):
    u_input = sys.stdin.readline().strip() 
    sudoku[r] = list(map(int, u_input))     
sudoku_zeros = [(i, j) for i in range(ROW) for j in range(COL) if sudoku[i][j] == 0]

def check_value(map, r, c, val):
    if val in map[r]:
        return False
    
    for r_idx in range(9):
        if map[r_idx][c] == val:
            return False
    
    rwise_start = (r//3) * 3    
    cwise_start = (c//3) * 3  
    # 3x3 매트릭스 범위 지정
    for rb in range(3):         # rb: ROW boundary
        for cb in range(3):     # cb: column boundary
            if map[rwise_start + rb][cwise_start + cb] == val:
                return False
    return True

def dfs_backtrace(zeros_index):
    '''
    param:
        - zeros_index = (r,c) of 0's from the zero_list
    rt_val:
        - no return value = only update vals in sudoku
    '''
    if zeros_index == len(sudoku_zeros):
        return True
    r_idx, c_idx = sudoku_zeros[zeros_index]
    for val in range(1, 10): 
        if check_value(sudoku, r_idx, c_idx, val):
            sudoku[r_idx][c_idx] = val 
            if dfs_backtrace(zeros_index + 1): 
                return True
            # backtrace
            sudoku[r_idx][c_idx] = 0 
    return False

dfs_backtrace(0)    # sudoku 에서 값이 '0' 인 원소들의 리스트 모두 체크
for r in sudoku:
    print(''.join(map(str, r)))