# 최단 경로 Dijkstra algorithm ( 특정 노드에서 모든 노드까지)
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# n = nodes, m = edge 유저 인풋 받기
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]

# 방문 처리 초기화
visited = [False] * (n + 1)
# 최단 거리 테이블도 초기화
dist_table = [INF] * (n + 1)

# 모든 edge 정보 입력받기(m)
for _ in range(m):
    curr, next, cost = map(int, input().split())    # current node / next node / cost (=distance info)
    graph[curr].append((next, cost))                # 현재 노드(curr)에 튜플로 (다음 노드 값, 노드 사이 거리) 삽입

# **방문하지 않은 노드** 중, 거리가 가장 짧은 노드의 인덱스 반환시키는 함수
def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, n + 1):   # 노드 1부터 n 까지 하나씩 확인
        if dist_table[i] < min_val or not visited: 
            min_val = dist_table[i]
            idx = i
    return idx

# 준비 다 끝났으니 최단거리 찾기 시작
def dijkstra(start):
    # 시작 노드 distance 와 방문 여부 초기화
    dist_table[start] = 0
    visited[start] = True

    # 호.. 어렵다
    for j in graph[start]:
        dist_table[j[0]] = j[1] # 아하 현재 노드에서 다음 노드로 가는 가장 빠른 경로 j[1] 업데이트 시키는거..?
    
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리 (앞에서 시작 노드 처리해준 것 처럼)
        curr = get_smallest_node()
        visited[curr] = True

        # 현재 노드와 인접한 다른 노드의 거리 확인
        for j in graph[curr]:
            next_distance = dist_table[curr] + j[1] # 현재 노드까지의 거리 + 그의 인접한 노드의 거리
            # 거리가 더 짧은 경우, 최소 거리 테이블 값 업데이트
            if next_distance < dist_table[j[0]]:
                dist_table[j[0]] = next_distance
            
# 최단 거리 구하기
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달 불가능한 경우, 출력 infinity
    if dist_table[i] == INF:
        print("INFINITY")
    else:
        print(dist_table[i])