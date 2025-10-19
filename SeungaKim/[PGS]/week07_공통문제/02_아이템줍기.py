# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 아이템줍기.py
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 9:01
    # rectangle = 2d list, (charX, charY) = 초기 위치, (itemX, itemY) = 아이템 위치
    # rectangel = maps [좌측하단 x, 좌측 하단 y, 우상단 x, 우상단 y]
    # start = (charX, charY)
    # target = (itemX, itemY)
    
    # 가장짧은 거리 찾기 -> bfs
    '''
        bfs 동작 순서
        1. 방문할 queue 생성
        2. visited 생성
        3. 첫 노드 queue 삽입 & 방문처리
        4. 방문할 노드 queue 에서 하나씩 꺼내기 (삽입순으로)
        5. queue 에서 꺼낸게 방문한 노드가 아니면, 인접 노드를 queue 에 삽입하고 방문처리
        ^. 끝날때까지 반복
        (+) 7. 사각형 좌표 위로 움직이는거
    '''
### Q. 가장 큰 의문점 >> 왜 좌표 맥스가 왜 102? 99 아니고? 
#       꼭지점끼리 맞붙지 않는다했는딩. (x, y) 범위는 1 이상 50 이하인 자연수
    MAX_LENGTH = 102 # ??

    answer = 0
    # 1. queue
    dq = deque()
    # 2. visited
    # visited = [[False] * len(rectangle[0]) for _ in range(len(rectangle))]
    visited = [[False] * MAX_LENGTH for _ in range(MAX_LENGTH)] 
    # print(visited)
    # map = [[0] * len(rectangle[0]) for _ in range(len(rectangle))]
    map = [[0] * MAX_LENGTH for _ in range(MAX_LENGTH)] 
    
    # 3.
    # Q. *2는 왜??
    dq.append((characterX * 2, characterY * 2, 0)) # 시작 포인트 + 스텝 카운트
    visited[characterX * 2][characterY * 2] = True

    # 7.
    def move(lb_x, lb_y, rt_x, rt_y):   # [좌측하단 x, 좌측 하단 y, 우상단 x, 우상단 y]
        # 왜 좌표를 2배씩해주는걸까.. 좌표 * 2 는 전부 gpt 도움!
        lb_x, lb_y, rt_x, rt_y = lb_x * 2, lb_y * 2, rt_x * 2, rt_y * 2
        for x in range(lb_x, rt_x + 1):
            for y in range(lb_y, rt_y + 1):
                if lb_x < x < rt_x and lb_y < y < rt_y:
                    # 안이면
                    map[x][y] = 2
                elif map[x][y] != 2:    # 사각형 안이 아닐 때,
                    map[x][y] = 1

    # map update
    for rect_coordinate in rectangle:
        move(*rect_coordinate) # rect -> *rect : gpt 도움
        '''move(rect) -> move([1, 1, 7, 4])
            move(*rect) -> move(1, 1, 7, 4)'''
    
    def is_map(r, c):
        output = False
        # if 0 <= r <= range(100) or 0 <= c <= range(100) or map[r][c] == 1:
        if 0 <= r < MAX_LENGTH and 0 <= c < MAX_LENGTH and map[r][c] == 1:
            output = True
        return output
    
    # 상하좌우 체크
    r_wise = [-1, 1, 0, 0]
    c_wise = [0, 0, -1, 1]
    
    while dq :
        r, c, answer = dq.popleft()
        # 정지 컨디션
        if (r, c) == (itemX * 2, itemY * 2):    # 대체 왜요?
            return answer // 2
        
        # for rect_coordinate in rectangle:
        #     move(rect_coordinate) #  여기가 아니였음! -> gpt

        # 새로운 위치 포지션 갈 수 있는가 체크
        for i in range(4):
            new_r = r_wise[i] + r
            new_c = c_wise[i] + c
            # 가능이면 인접 노드들 dq 에 삽입 + 방문처리
            if is_map(new_r, new_c) and not visited[new_r][new_c]:
                dq.append((new_r, new_c, answer + 1))   # 1arg -> tuple 로 묶어
                visited[new_r][new_c] = True 

    # 만약 target point 안 가고 그냥 끝났으면,
    return -1

# test input
rectangle =  [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY	= 3
itemX = 7
itemY = 8
# result = 17
print(solution(rectangle, characterX, characterY, itemX, itemY))
# 10:03