#https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 16:55
'''
S : 시작 지점
E : 출구
L : 레버
O : 통로
X : 벽

출발점 -> 레버
레버 -> 출구
'''
from collections import deque
# deque 쓰면 이건 bfs <-> recursive 쓰면 dfs고

def bfs(maps, start, target):
    '''
    parameters
        - maps : 2d list by user inptu
        - start : starting point coordinate
        - target : target point coordinate ( stop when its target, and print count)
    rt_val
        - none: fully visited maps
    '''
    dq = deque() 
    dq.append((start[0], start[1], 0))     # ((coordinates(r, c), step_counts))


    # init visited as 0 for all
    visited = [[False] * len(maps[0]) for _ in range(len(maps))] 
    visited[start[0]][start[1]] = True  # 2d list 니까 , 말고 [][]
    # 최단거리찾기..전에!
    direct_row = [-1, 1, 0, 0]
    direct_col = [0, 0, -1, 1]
    # 또 그 전에!
    def is_path(r, c):
        path = False
        if 0 <= r < len(maps) and 0 <= c < len(maps[0]) and not visited[r][c] and maps[r][c] != 'X':
            path = True
        return path

    while dq:
        r, c, cnt = dq.popleft()    # 들어간 순서대로 빼내기

        if (r, c) == target:
            return cnt
        # 아니라면, 계속 위치 업데이트
        for x in range(4):  # 상하좌우
            new_r = direct_row[x] + r
            new_c = direct_col[x] + c
            if is_path(new_r, new_c):
                visited[new_r][new_c] = True
                dq.append((new_r,new_c, cnt + 1))   # 똑같이, (((r, c), step_count))

    return -1

def solution(maps):
    answer = None
    lever = None
    exit_pos = None
    for r in range(len(maps)):
        for c in range(len(maps[0])):  # 에헤이 오류메세지나면 읽자
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'E':
                exit_pos = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
                
    # 출발점에서 레버까지 최단거리 찾기 -> 최단거리(BFS)
    step_cnt_lever = bfs(maps, start, lever)
    if step_cnt_lever == -1:
        return -1
    # 레버에서 출구 찾기
    step_cnt_exit = bfs(maps, lever, exit_pos)
    if step_cnt_exit == -1:
        return -1
    answer = step_cnt_lever + step_cnt_exit

    return answer
