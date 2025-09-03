# Min Spanning Tree : Kruskal's algorithm
# 최소한의 비용으로 -사이클 없이- 존재하는 모든 노드 연결시키기 = kruskal

def find_parent(parent, a):
    # find root node
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, b, c):
    c = find_parent(parent, c)
    b = find_parent(parent, b)
    if c > b:
        parent[c] = b
    else:
        parent[b] = c

# get parent info (v, e)
# node nums = n 으로 했는데, 생각해보니 헷갈릴 수 있어서 그래프 노드 개수는 v 로 공용화해서 쓰는것 같음
v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v + 1):  # init parent table
    parent[i] = i

# 모든 간선을 담을 리스트 & 최종 비용 변수
edges = []
final_cost = 0

# 모든 간선에 대해 정보-비용- 받아 업데이트
for _ in range(e):
    b, c, cost = map(int, input().split())
    # 비용순 오름차순으로 정렬.. 하기 위해서 튜플의 첫 번째 원소를 cost 로 설정
    edges.append((cost, b, c))

edges.sort()    # 비용순 오르ㅁ차순으로 정렬

# 간선 하나씩 확인하면서 사이클 발생하지 않을 때만 min spanning treㄷ 에 넣음. 나머지는 무시
for edge in edges:
    cost, b, c = edge   # assign val of tuple
    # 사이클 발생하지 않는 경우만 집합에 넣어줌
    if find_parent(parent, b) != find_parent(parent, c):
        union_parent(parent, b, c)
        final_cost += cost
    # else:

print(final_cost)
