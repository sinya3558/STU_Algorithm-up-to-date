#00:37:50.13
import sys
from collections import deque

#sys.stdin = open("input.txt", 'r')

'''
정점 N개, 간선 M개인 그래프 탐색하는 문제 (양방향)
- 그래프의 노드의 연결관계 표현하기 위해 dict로 graph 초기화
    - 특정 노드는 key
    - 특정 노드에 연결된 노드는 여러개 일 수 있으므로 list로 초기화해서 value append
    - 연결된 노드가 여러개면 오름차순으로 방문하므로 각 value list 오름차순 정렬
- DFS는 재귀적으로 구현
- BFS는 큐를 이용해 구현
'''

N, M, V= map(int, sys.stdin.readline().split())

# 그래프 초기화 1~N까지
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    key, value = map(int, sys.stdin.readline().split())
    # 양방향 간선
    graph[key].append(value)
    graph[value].append(key)
#print(graph)

for i in range(1, N + 1):
    graph[i].sort()

# curr_node: 현재 방문중인 노드, visited: 방문한 노드 추적하는 집합
def DFS(curr_node, graph, visited):
    visited.add(curr_node) # 방문한 노드 표시
    print(curr_node, end=" ") # 방문한 노드 출력
    for next in graph[curr_node]: # 현재 노드와 연결된 노드 탐색
        if next not in visited: # 방문하지 않은 노드라면
            DFS(next, graph, visited) # 재귀적으로 DFS 호출
    return 0
# starte_node: 탐색 시작하는 노드
def BFS(start_node, graph):
    queue = deque([start_node]) # 시작 노드 큐에 넣음
    visited = set([start_node]) # 시작 노드 방문 표시
    print(start_node, end=" ") # 시작 노드 출력
    
    # 큐에 노드 있는 동안 계속 탐색
    while queue:
        cur = queue.popleft() # 큐에서 노드 하나 꺼내서
        #print(bool(queue))
        for next in graph[cur]: # 연결 노드 모두 탐색
            if next not in visited: # 방문하지 않은 노드라면
                visited.add(next) # 방문했다고 표시
                queue.append(next) # 큐에 추가
                print(next, end=" ") # 방문한 노드 출력

    return 0

visited_dfs = set()
DFS(V, graph, visited_dfs)
print()
BFS(V, graph)
print()