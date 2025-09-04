# https://www.acmicpc.net/problem/2239 
import sys
# get user input
row = 9 
col = 9
sudoku = [[0] * col for _ in range(row)]
for r in range(row):
    u_input = sys.stdin.readline().strip() 
    sudoku[r] = list(map(int, u_input))     
sudoku_zeros = [(i, j) for i in range(row) for j in range(col) if sudoku[i][j] == 0]

def check_value(map, r, c, val):
    if val in map[r]:
        return False
    
    for r_idx in range(9):
        if map[r_idx][c] == val:
            return False
    
    rwise_start = (r//3) * 3    # (idx 0, 3, 6)
    cwise_start = (c//3) * 3  # (idx 0, 3, 6)
    # 3x3 매트릭스 범위 지정
    for rb in range(3):         # rb: row boundary
        for cb in range(3):     # cb: column boundary
            if map[rwise_start + rb][cwise_start + cb] == val:
                return False
    return True

def dfs(zeros_index):
    if zeros_index == len(sudoku_zeros):
        return True
    r_idx, c_idx = sudoku_zeros[zeros_index]
    for val in range(1, 10): 
        if check_value(sudoku, r_idx, c_idx, val):
            sudoku[r_idx][c_idx] = val 
            if dfs(zeros_index + 1): 
                return True
            sudoku[r_idx][c_idx] = 0 
    return False

dfs(0)