# 합승 택시 요금 (2021 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3
def solution(n, s, a, b, fares):
    '''
    INPUTS
    n : nums of nodes
    s : starting point
    A, B : diff destinations
    fares[2d int 요금 array] = expected taxi fees / len(fares) =  n x (n-1) / 2 
        - [5, 7, 9] -> 노드 5 랑 7 사이 요금이 9원
        - [4, 6, 4] -> 노드 4 랑 6 사이 요금이 4원
        - [3, 6, 1] -> 3 과 6 사이 요금이 1원..
    OUTPUTS
    14(min. sum of fares)
    '''
    # check inputs n
    if not 3 <= n <= 200:
        raise ValueError("invalid input n")
    # check size of fares
    if not len(fares) <= n * (n-1) / 2 :
        raise ValueError("invalid input fares")
    
    # 일단, 이게 어떤 알고리즘이 필요함?? 투포인터? 최단거리 찾기 -> dijkstra
    '''
    dijkstra
    1. set up starting point
    2. init shortest path table
    3. select closest node if its not visited
    4. cal cost from node to another
    4. repeat step 3-4 -> update shortest path w new cost
    '''
    # declare vars
    answer = 0
    tb_shortest_path = []
    INF = int(1e6)                              # fares의 값이 100000이하 자연수여야함
    # visited = [False] * (n + 1)         # 방문 거리 초기화 ---> 이하 동문입니다. 여기말고 사용 함수 안에다 적어야지
    # tb_shortest_path = [INF] * (n + 1)  # 최단 거리 테이블도 초기화 -> 얘 땜에 테이블 초기화 안되서 에러남ㅋㅋㅋㅋㅋㅋㅋ 바보야
    info = [[] for _ in range( n + 1 )]   # 노드 정보(번호, 거리) 담을 리스트

    # # fares 값 모두 입력받기
    for idx in range(len(fares)):
        curr, next, cost = map(int, fares[idx])
        # print(curr, next, cost)
        info[curr].append((next, cost))     # (next node num, cost(=distance))
        info[next].append((curr, cost))     # (curr node num, cost(=distance)), curr <-> next 순서 상관 없긴한데.. 괜찮나?


    # min 거리의 노드 인덱스 반환시켜 -> ***방문하지 않은 노드*** 중에서
    def get_min_idx(tb_shortest_path, visited):
        min_val = INF
        min_idx = -1    # 0 했다가 에러남. invalid 하려고 (-1) 넣어버림
        for i in range(1, n+1):
            if tb_shortest_path[i] < min_val and not visited:
                min_val = tb_shortest_path[i]   # update
                min_idx = i
        return min_idx

    # 다익스트라
    def dijkstra(start):
        # declare 'path-table' and 'visited' status as local vals to init whenever its called
        tb_shortest_path = [INF] * (n + 1)
        visited = [False] * (n + 1)
        # init start node & visited
        tb_shortest_path[start] = 0
        visited[start] = True

        for _ in range(n):
            curr = get_min_idx(tb_shortest_path, visited)    # find min dist(=cost)
            if curr == -1:  # invalid 할때
                break
            visited[curr] = True    # 방문처리

            for next, cost in info[curr]:    # curr 노드와 인접한 노드의 거리 체크
                new_dist = tb_shortest_path[curr] + cost
                if new_dist < tb_shortest_path[next]:
                    tb_shortest_path[next] = new_dist

        return tb_shortest_path

    # dijkstra(s)
    # s -> e 최단 거리 테이블 구해버리기
    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)

    # 합승 지점을 k로 했을 때 최소 요금 계산
    answer = INF
    for k in range(1, n + 1):
        answer = min(answer, dist_s[k] + dist_a[k] + dist_b[k])

    return answer

