# https://www.acmicpc.net/problem/2239 
# 16:56
# 인풋이 엄청 많음 -> readline
import sys
# get user input
row = 9 # 3 for test
col = 9
# u_input = sys.stdin.readlines()  # .strip()은 '\n' 무시하게 만드는거라 이 경우에 안 썼음 ---> readline() 쓰는게 mem eff 더 좋구나

# sudoku = [[] * col for _ in range(row)] # only empty 2d list
sudoku = [[0] * col for _ in range(row)]
for r in range(row):
    u_input = sys.stdin.readline().strip()  # 한 줄 통으로 하나씩 받아서 처리 -> 메모리 효율적
    sudoku[r] = list(map(int, u_input))     # convert str -> list(int)

# sudoku_zeros = [(r, c) for i in range(row) and for j in range(col) if sudoku[i][j] == 0]  # 위치 안변하니까 튜플
sudoku_zeros = [(i, j) for i in range(row) for j in range(col) if sudoku[i][j] == 0]
# print(sudoku_zeros)

# dfs? bfs? 아님 행,렬은 dfs 쓰고 3x3 은 bfs?
# dfs(graph, v(#node), visited) -> 근데 0 아니면 그냥 패스하면 되서 빠르게 체크만 하면될듯
''' 일단 체크 리스트
    1. 스도쿠 맵 바운더리 체크
    2. board[r][c] == 0 애들만 따로 위치 저장 (TC)
    3. 현재 값이 0인 포지션에 1 ~ 9 사이에서 알맞은 값 val 찾아서 대입
        -> 여기서 val 찾을 떄 backtracking 씀
        backtracking : 조건 만족하면 패스, 아니면 빠꾸. 다시 이전 값 제외한 val 수 찾기
    4. 근데 3x3 matrix 어떻게 체크함? bfs?? '''
# 18:17

# 21:24
def check_value(map, r, c, val):
    '''
    parameter : map(sudoku board), r(row), c(column), val(value for map[r][c])
    rt_val : boolean

    잉, 0 값 자리에 넣어줄 val 도 같이 넣어줘야하네
    목표는 map[r][c] 자리에 val 알맞은가 찾는 거
    '''
    # for r_idx in range(9):
    #     if map[r_idx][c] != val:
    #         for c_idx in range(9):
    #             if map[r][c_idx] != val:
    #                 # 이 경우는 map[r][c] 에 val 입력 가능. 근데 이렇게 nested loop 써도 되나..
    #                 return True
    # return False
    
    # check row line
    if val in map[r]:
        return False
    # check col line -> 아, r 에 해당하는 c 다 체크 해야됨, 0에서 8까지 (그림 그리면 이해됨요)
    for r_idx in range(9):
        if map[r_idx][c] == val:
            return False
    
    # check 3x3 mini matrix (노트)
    # 일단 row index 를 감싸는 3x3 범위 정하기(0 ~ 8 사이)
    rwise_start = (r//3) * 3
    # column wise starting index
    cwise_start = (c // 3) * 3  # (idx 0, 3, 6)
    # 3x3 매트릭스 범위 지정
    for rb in range(3):         # rb: row boundary
        for cb in range(3):     # cb: column boundary
            # 범위 안에 val 존재하면,
            if map[rwise_start + rb][cwise_start + cb] == val:
                return False
            
    # 그 외는 모두 val 넣어라
    return True


def dfs(zeros_index):
    # dfs(board) 해야되냐 아님 dfs(position) 해야하나
    if zeros_index == len(sudoku_zeros):    # list of tuple(zeros) 끝까지 훑으면 종료
        return True
    # while sudoku_zeros:
    #     # 0 인 값들이 다 채워질때까지 진행
    #     for r_idx in range(len(sudoku_zeros)):
    #         for c_idx in range(len(sudoku_zeros)):
    #             # 1~ 9 사이 알맞은 값이 들어갔는지 확인
    #             for num in range(1, 9):    
    #                 sudoku_zeros[r_idx][c_idx] # 아니 이거 아닌 것 같음 백퍼 오류남
    r_idx, c_idx = sudoku_zeros[zeros_index]
#     print(f'row=',r_idx, f'col=',c_idx)
# dfs(0)
    for val in range(1, 10): # 1 ~ 9 사이에서 알맞는 값 찾을 떄까지 진행
        if check_value(sudoku, r_idx, c_idx, val):
            sudoku[r_idx][c_idx] = val  # 0 업데이트
            # zeros_index += 1
            # dfs(zeros_index)
            if dfs(zeros_index + 1):  # 안정성
                return True
            sudoku[r_idx][c_idx] = 0  # 실패하면 되돌리기(!!!)
        # 나머지는 패스
    return False
    # 왜 틀린걸까
    # 23:22
dfs(0)

# 일단 내일 할거
'''
- 시간초과 에러 해결
- dfs() 손보고 출력값 프린트
'''