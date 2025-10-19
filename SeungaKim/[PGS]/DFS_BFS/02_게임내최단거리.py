# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임내최단거리.py

from collections import deque
# bfs, dfs 하려면 필요한 거 == graph, visited, start_node

def solution(maps):
    # answer = 0
    try :
        if not 1 <= len(maps) <= 100:
            raise ValueError
        if not 1 <= len(maps[0]) <= 100:
            raise ValueError
        if not all(cell in (0, 1) for row in maps for cell in row):
            raise ValueError
        
        '''
        bfs 동작 순서
        1. 방문할 queue 생성
        2. visited 생성
        3. 첫 노드 queue 삽입 & 방문처리
        4. 방문할 노드 queue 에서 하나씩 꺼내기 (삽입순으로)
        5. queue 에서 꺼낸게 방문한 노드가 아니면, 인접 노드를 queue 에 삽입하고 방문처리
        ^. 끝날때까지 반복
        '''
        
        # 그 전에, 
        def is_path(r, c) : #  0은 벽이 있는 자리, 1은 벽이 없는 자리
            path = False
            if 0 <= r < len(maps) and 0 <= c < len(maps[0]) and not visited[r][c] and maps[r][c] == 1:
                path = True
            return path
        row_wise = [-1, 1, 0, 0]
        col_wise = [0, 0, -1, 1]

        # 1ㅡ2
        dq = deque()
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        '''
        visited = []
        for i in range(len(maps)):
            row = []
            for j in range(len(maps[0])):
                row.append(False)
            visited.append(row)
        '''
        step_cnt = 1
        # first_coord = (0, 0)  # (1, 1)
        # target_coord = (4, 4)   # (5, 5)
        target_coord = (len(maps) - 1, len(maps[0]) - 1)    #  (4, 4)는 테스트케이스에서 다 실패함

        # 3-
        dq.append((0, 0, step_cnt))    # 시작 지점 (1,1)
        visited[0][0] = True

        while dq:
            row, col, step_cnt = dq.popleft() # 4
            if (row, col) == target_coord:
                return step_cnt
            # 아니라면, 반복
            for x in range(4):   # 상하좌우 체크
                # 업데이트 위치
                new_row = row_wise[x] + row
                new_col = col_wise[x] + col
                # validation    
                if is_path(new_row, new_col):
                    visited[new_row][new_col] = True    # 5
                    dq.append((new_row, new_col, step_cnt + 1)) # 5

    except Exception as e:
        print(f"Invalid input data, {type(e)}")
        return 0

    return -1

map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(map))