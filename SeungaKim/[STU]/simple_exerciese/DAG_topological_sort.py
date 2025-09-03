# DAG : Direct acyclic graph
# topological sort : 큐에 들어간 순서대로 topological sort 결과값이 됨
# TS 의 원리는 뭐냐? 사이클이 없는 방향 그래프의 모든 노드를 "" 방향성에 거스르지 않도록""" ""순서대로 나열""시키는 거
# college pre-requisite courses 용

# queue 사용 필수
from collections import deque

v, e = map(int, input().split())
# 모든 노드에 대한 연결차수? 진입차수? Indegree = 0 으로 init
i_degree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보 담기위해 init linked list
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    node_a, node_b = map(int, input().split())    # info : (node_a, node_b), A -> B 연결되는 방향성 있는 간선
    graph[node_a].append(node_b)
    # 진입 차수 1증가
    i_degree[node_b] += 1   # A 에서 들어오니까


def topological_sort():
    result = [] # 큐 입력 순서를 빼내서 입력해둘 결과 리스트
    queue = deque()

    # indgree = 0 인 노드는 무조건 queue 에 삽입
    for i in range(1, v+1):
        if i_degree[i] == 0:
            queue.append(i) #queue.append[i]
    # 큐가 빌 때까지 루프
    while queue:
        # 큐에서 삽입한 원소 꺼내기
        popped_node = queue.popleft()
        result.append(popped_node)

        # 제거된 노드에서 나오는 edge 간선들 제거하기, 그리고 indegree = 0? 큐에 집어넣기
        for i in range(popped_node):
            i_degree[i] -= 1
            # 먄약 indgree = 0?
            if i_degree[i] == 0:
                result.append(i)
    
    # print final result
    for node in result :
        print(node, end=' ')

topological_sort()