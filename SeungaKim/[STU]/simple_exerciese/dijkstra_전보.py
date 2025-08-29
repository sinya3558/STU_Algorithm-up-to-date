# 전보 보내기
'''
- N개의 도시가 있다. X->Y 도시로 전보를 보내려면, X에서 Y로 향하는 통로가 설치되어 있어야 한다
Y에서 X로 향하는 통로가 없다면 Y는 X로 메세지를 보낼 수 없다( =edge direction)
- 또 통로를 거쳐 메세지를 보낼 때는 일정 시간이 소요된다( =cost)
- C도시에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, **메세지를 보낼 때 최대한 많이 퍼질 것이다**, 그 메세지를 받게 되는 도시의 개수와 걸리는 시간을 계산하여라.

입력조건
- 첫째 줄에 도시 개수 n, 통로 개수 m, 메세지 보내고자 하는 도시 c
- 둘째 줄부터 m + 1 번째 줄에 걸쳐 통로에 대한 정보 X,Y,Z 주어진다. 
    이는 도시 X에서 다른 도시 Y로 이어지는 통로가 있으며, 메세지 전달 시간이 Z
출력조건
- 도시 C에서 보낸 메세지를 받는 도시의 총 개수와 걸리는 시간 공백으로 구분하여 출력

input
3 2 1
1 2 4
1 3 2
output
2 4
'''
# 문풀 아이디어
# 다익스트라 문제인듯 (노드 하나에서 다른 여러개의 노드까지의 거리)
# 그럼 우선순위 큐 -> 최단 거리라서 min heap(defaut) 로 처리
# 11:58
import heapq
import sys

input = sys.stdin.readline  # 한꺼번에 다 받아
INF = int(1e9)  # 거리 테이블 초기화 ㅛㅇㅇ

n, m, c = map(int, input().split())
# cost 랑 노드 번호 저장할 리스트? 그래프? 만들기
graph = [[] for _ in range(n + 1)]  # 노드 1부터 시작이니까
# 최단 거리 테이블 초기화
dist_table = [INF] * (n + 1)

# 엥 왜 따로 만들어? -> 아하 그래프에 모든 edge 정보 입력
for _ in range(1, m + 1):
    x, y, z = map(int, input().split())
    # print(x, y, z)
    graph[x].append((y,z))  # (다음 나라 노드, cost) 튜플 구조로 삽입 -> 힙에 삽입하기 이전


# 다익스트라 알고리즘 함수
def dijkstra(start):
    pq = []
    # 우선순위 큐에 넣을 것 -> 방문하지 않은 노드의 (인접 노드 번호, 거리 코스트)
    # 일단 처ㅓ음 시작 노드 설정
    heapq.heappush(pq, (0, start))  # Q. 왜 굳이 이 순서지? 반대로 (노드#, cost) 하면 안되??
    dist_table[start] = 0 # 초기 노드 거리 0 -> 자기 자신에서 자기 자신으로 이동하니 0

    # 우선순위 큐 입력과 삭제하면서 최단 거리 비교
    while pq : 
        dist, curr_node = heapq.heappop(pq)
        if dist_table[curr_node] < dist: # dist[curr_node] 같이 생각없는 실수 하지마 그냥
            # 최소 거리 값 갱신 안되면 -> 무시
            continue
        # 아니라면, 현재 노드와 인접한 노드들과의 거리 모두 계산
        for i in graph[curr_node]: # 현재 노드에서 인접한 애들 다 불러서
            # dist_table[i[0]] = min(dist_table[i[0]], dist_table[i[0]] + i[1]) 
            sum_distance = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우,
            if dist_table[i[0]] > sum_distance:
                # 해당 노드의 최단 거리 갱신
                dist_table[i[0]] = sum_distance
                # 우선순위 큐 삽입
                # heapq.heappushpop(cost_distance, i) # 바보냐. 삽입하라면서 pop을 왜햐......
                heapq.heappush(pq, (sum_distance, i[0]))

# func call
dijkstra(c) # 도시 C가 시작노드

# print out result
# 도달 가능한 도시의 수
cnt_countries = 0
# 도달 가능 도시들 중에서 가장 멀리 있는 나라와의 최단 거리
max_dist = 0
for i in dist_table:
    if i != INF:
        cnt_countries += 1
        max_dist = max(max_dist, i) # 최대로

# **시작노드 제외**해야하니 -1
print(cnt_countries - 1, max_dist)
# 1:49