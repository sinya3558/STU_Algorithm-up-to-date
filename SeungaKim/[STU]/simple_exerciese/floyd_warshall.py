# 최단거리 알고리즘 : Floyd-Warshhall
# 모든 노드에서 다른 모든 노드를 거치면서 최단 ㄱ거리 구하기

INF = int(1e9)  # 최단 거리 테이블 초기화값을 위한 inf

# n, m input
n = int(input())    # n = nums of nodes
m = int(input())    # m = nums of edges

# 2d list(graph) 만들고, INF 값으로 테이블 초기화 -> floyd warshall 은 2d 테이블에 최단거리 정보 저장 (<-> dijkstra 와 차이점)
graph_2d = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 identical 행렬은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph_2d[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 최단거리 테이블 초기화 (갱신 가능한 경우만)
for _ in range(m):
    # a -> b : c (=cost) 라고 설정
    a, b, c = map(int, input().split())
    graph_2d[a][b] = c

# 플로이드 워셜 알고리즘 - 3 nested for loop -> .Q. 그럼 얘 O(N^3) 아닌가.. 타임에러 각인데 얘를 대체 왜?
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph_2d[a][b] = min(graph_2d[a][b], graph_2d[a][k] + graph_2d[k][b])   # 1.(a->b) 거리와 2.(a->k 지나 k->b)까지의 거리 비교
        
# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달 불가능의 경우, infinity
        if graph_2d[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            # 도달 가능한 경우, 실제 최단 거리 출력
            print(graph_2d[a][b], end=" ")
    print()