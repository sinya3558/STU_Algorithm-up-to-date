# find cycle or identify cycel from disjoint set

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b   # update smaller value
    else:
        parent[b] = a

# set up num of nodes and edges
n, e = map(int, input().split())
# init parent table
parent = [0] * (n + 1)

# init values of parent table by itself
for i in range(1, n + 1):
    parent[i] = i

# init 사이클 발생 여부
cycle = False   

for i in range(e):  # 두개의 노드를 지나는 엣지를 하나씩 확인하면서,
    node_a, node_b = map(int, input().split())
    # 사이클 발생한 경우, 종료
    if find_parent(parent, node_a) == find_parent(parent, node_b):
        cycle = True
        break   # 아닛 reutrn 이 무슨 왜 나와..
    # 사이클 발생하지 않은 경우, union 연산 수행
    else:
        union_parent(parent, node_a, node_b)

if cycle:
    print("cycle : true")
else:
    print("cycle : false")