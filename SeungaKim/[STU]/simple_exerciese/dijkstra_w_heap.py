# dijstra algorithm with heap data structure
# 거리가 가장 짧은 노드 선택 -> min heap
# 설명 노션이 있음
import sys
import heapq

# input
input = sys.stdin.readline
INF = int(1e9) # 큰 수 설정(10억)

# 노드 n, 간선(edge) e 의 개수 
n, e = map(int, input().split())

# STEP 0 : 시작 노드 입력
start = int(input())
# graph : 노드에 연ㄱ결되어있는 정보(노드 번호, 거리) 담는 리스트 만들기
graph = [[] for i in range(n + 1)]  # 1번 노드부터 담을거라
# 최단 거리 테이블 INF 로 초기화
dist_table = [INF] * (n + 1)        # 여기도 마찬가지. 1번 노드부터 담을거

# 노드를 연결시켜주는 모든 간선(edge) 정보 입력받기
for _ in range(e): 
    curr, next, cost = map(int, input().split())
    # curr node ->(cost)-> next node
    graph[curr].append((next, cost))    # (next node number, cost(=distance)) 튜플 값으로 지정해 저장 -> 안변하니까


# 최단 거리 구하기
def dijkstra(start):
    pq = []  # priority queue
    # init start node -> 노드 1에서 노드 1까지의 거리 '0' 설정해준 뒤, 우선순위 큐에 넣기
    # pq.append() 가 아니지 바보야
    heapq.heappush(pq, (0, start))  # ㅇ선순위 큐에 노드1(=start) 정보 - 거리랑 노드번호 - 삽입
    dist_table[start] = 0           # 최단 거리 테이블에 시작 노드 값 '0' 지정

    # 그 외 나머지 노드들에게
    while pq :  # 우선순위가 비어있지 않다며ㅕㄴ,
        # 최단 거리의 노드 정보(거리(=코스트), 노드 번호) 꺼내서 처리하기 -> 이거 순서 까먹지 마라잉
        dist, node_num = heapq.heappop(pq)
        # 이미 처리 되서 최단 거리가 지정된 노드라면 -> 무시
        if dist_table[node_num] < dist:
            continue
        # 현재 노드와 연결된 인접 노드들 확인
        for i in graph[node_num]:
            sum_dist = dist + i[1]  # 현재 노드까지의 거리(=dist) + 그와 인접한 다음 노드까지의 거리(=i[1])
            # 만약 현재 노드를 거쳐서, 인접한 다음 노드까지 이동하는 거리가 더 짧을 경우 -> 최단 거리 테이블 값 갱신
            if sum_dist < dist_table[i[0]]:
                dist_table[i[0]] = sum_dist # 최단 거리
                # 그리고 튜플 정보(거리, 노드 넘버) 우선순위 큐에 삽입
                heapq.heappush(pq, (sum_dist, i[0]))
                # Q. 솔직히 i[0], i[1] 정확하게 뭘 말하는지 헷갈림. 거리 같은데 또 노드 번호 같기도 하고...

# main func
dijkstra(start)
# 모든 노드로 가기위한 최단거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, infinity
    if dist_table[i] == INF:
        print("INFINITY")
    else:
        print(dist_table[i])
        print(f'node', i, ': distance :', dist_table[i])