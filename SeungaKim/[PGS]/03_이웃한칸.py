# https://school.programmers.co.kr/learn/courses/30/lessons/250125?language=python3
'''
보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 
고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때
board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요
'''
def solution(board, h, w):
    # constraints
    if not (1 <= len(board) <= 7):
        raise ValueError("invalid input(board)")
    if not( 0<= h < len(board)) or not (0 <= w < len(board[0])):
        raise ValueError("invalid input(h, w)")
    if not (1 <= len(board[h][w]) <= 10) or not(board[h][w].islower()):
        raise ValueError("invalid input")
    
    # board = 색깔 이름이 당긴 문자열 리스트
    # init values
    dir_w = [0, 0, -1, 1]
    dir_h = [-1, 1, 0, 0]
    answer = 0
    color_str = board[h][w]
    
    # starting point, board[h][w]
    # check position
    for i in range(4): # 상하좌우만 체크 -> range(len(board)) 했다가 runtimeError 봤다
        new_w = w + dir_w[i]
        new_h = h + dir_h[i]
        # check boundary
        if 0 <= new_w < len(board) and 0 <= new_h < len(board):
            if board[new_h][new_w] == color_str:
                answer += 1

    return answer