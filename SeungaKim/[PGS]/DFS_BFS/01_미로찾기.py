#https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 16:55
'''
S : 시작 지점
E : 출구
L : 레버
O : 통로
X : 벽
딱 보아하니 DFS/BFS 문제
출발점 -> 레버
레버 -> 출구
'''
import sys
# 인풋 문자열 리스트로 받는거 참고
import json
from collections import deque
# deque 쓰면 이건 bfs <-> recursive 쓰면 dfs고

def bfs(map, start, target):
    '''
    parameters
        - map : 2d list by user inptu
        - start : starting point coordinate
        - target : target point coordinate ( stop when its target, and print count)
    rt_val
        - none: fully visited map
    '''
    # declare deque as dq
    dq = deque() 
    first = [start[0],start[1]] # == starting point 의 (r, c)
    dq.append((first, 0))     # ((coordinates(r, c), step_counts))
    # 튜플튜플픁플.. 아 머리 터진당

    # init visited as 0 for all
    visited = [[False] * len(map[0]) for _ in range(len(map))]  # len(map[0]) = length of (map 의 첫번째 row's values, which is # of col)
    visited[first] = True
    # 최단거리찾기..전에! set up direction
    direct_row = [-1, 1, 0, 0]
    direct_col = [0, 0, -1, 1]

    while dq:   # 아, while map 인줄 알았는데.. 아니엿당
        r, c, cnt = dq.popleft()

        if (r, c) == target:
            return cnt
        # otherwiese,
        for old_r in direct_row:
            for old_c in direct_col:
                # update current position
                new_r = old_r + r
                new_c = old_c + c
                if 0 <= new_r < len(map) and 0 <= new_c < len(map[0]) and not visited[new_r][new_c]:
                    if map[new_r][new_c] != 'X':   # 벽이면,
                        visited[new_r][new_c] = True
                        dq.append((new_r,new_c, cnt + 1))   # 똑같이, (((r, c), step_count))
    
    return -1

def solution(maps):
    answer = 0

    # assign val from the user input
    for r in range(len(maps)):
        for c in len(maps[c]):  # 열이니까
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'E':
                exit = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
    # 출발점에서 레버까지 최단거리 찾기 -> 최단거리(BFS)
    step_cnt_lever = bfs(maps, start, lever)
    if step_cnt_lever == -1:
        return -1
    # 레버에서 출구 찾기
    step_cnt_exit = bfs(maps, lever, exit)
    if step_cnt_exit == -1:
        return -1
    answer = step_cnt_lever + step_cnt_exit

    return answer

# Read user input from 'input.txt'
maps = json.loads(input())
# print(maps)
# 17:05
# 17:55
# 19:39
# 예... 에러나구요. 일단 저장하고 to be continued 한다