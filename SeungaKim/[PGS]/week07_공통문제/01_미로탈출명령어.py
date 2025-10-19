# https://school.programmers.co.kr/learn/courses/30/lessons/150365
# 미로탈출명령어.py
# 12:24
from collections import deque
def solution(n, m, x, y, r, c, k):
    # Start : (x, y)
    # End : (r, c)
    # nxm maze
    # k : distance(steps)
    # 문자열 사전 순으로 빠른 경로로 탈출, "lul" = 왼쪽으로 한 칸, 위로 한 칸, 왼쪽으로 한 칸

    # 상하좌우 한 칸씩 이동
    # r_wise = [-1, 1, 0, 0]
    # c_wise = [0, 0, -1, 1]

    # 미로 구성
    # maze = ['.' * m for i in range(n)]
    # maze[x][y] = 'S'
    # maze[r][c] = 'E'
    # print(maze) # ['....', '....', '....']
    # k maximum 값이 2500 이라 bfs 로 돌리면 TimeError 날 수 ㅇ ㅣㅅㅆ음 -> greedy 

    # 문자열 상하좌우 -> ㄴㄴ
    # for str in maze:
    #     if str == 'l':
    #         move = (0, -1)
    #     elif str == 'r':
    #         move = (0, 1)
    #     elif str == 'u':
    #         move = (-1, 0)
    #     elif str == 'd':
    #         move = (1, 0)

    # dq = deque()
    # dq.append((x, y, 'S'))
    # 중복 방문 가능이라 visited ㄴㄴ

    
    # 이동 거리가 k 면서, S에서 E까지 이동할 수 있는 경로
    k_steps = abs(r - x) + abs(c - y)
    if k_steps > k :
        return 'impossible'

    # 아니라면, 
    # 문자열 상하좌우 테이블 !! 사전 알파벳순 정ㄹ렬
    moves = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

    # 갈 수 있는 길인지 확인
    def is_path(nx, ny):
        path = False
        if 1 <= nx <= n and 1 <= ny <= m:   # 두번이상 중복 가능
            path = True
        return path

    answer = ''
    curr_x, curr_y = x, y   # start point

    while k > 0:   # k가 0 될때까지
        for char, move_x, move_y in moves:
            new_x = curr_x + move_x
            new_y = curr_y + move_y
            # validation 
            if is_path(new_x, new_y):
                steps_left = abs(r - new_x) + abs(c - new_y)

                if steps_left <= k - 1:
                    answer += char # dlru
                    curr_x = new_x
                    curr_y = new_y
                    k -= 1
                    break

    return answer


# test input
n , m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5
# result = "dllrl"
print(solution(n, m, x, y, r, c, k))
# dllrl ...오.. 예상 아웃풋이 아닌뎅
# 2:12