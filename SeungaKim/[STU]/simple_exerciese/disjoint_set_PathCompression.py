# Find function for disjoint set with PATH COMPRESSION
# 원소의 루트 노드를 찾기 위해 부모 노드 테이블을 한번씩 다 재귀적으로 훑는게 아니라
# 원소의 루트 노드를 바로 찾고 그게 부모 노드가 되는 방식
# find_parent() 만 수정하면 가능 -> 시간 복잡도 감소

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을때까지 계속해서 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # keep on an update
    return parent[x]

# 두 원소가 속한 집합 union
def union_parent(parent, a, b): 
    a = find_parent(parent, a)  # find parent of element 'a'
    b = find_parent(parent, b)  # "" 'b'
    if a < b:
        parent[b] = a # 부모노드가 크면 작은 놈으로 업데이트
    else:
        parent[a] = b # ""

# 노드의 개수와 edeges 의 개수 입력 받기
v, e = map(int, input().split())    # v = 노드의 개수, e = edges의 개수
parent = [0]*(v + 1)

# 부모 테이블 init -> 자기 자신
for i in range(1, v + 1):   # 아.. 자꾸 range(v + 1) 만 쓸래?
    parent[i] = i

# Union two nodes
for i in range(e):
    node_a, node_b = map(int, input().split())
    union_parent(parent, node_a, node_b)

# 각 원소가 속한 집합 프린트
print(f'각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')  # 최종 리턴값만 프린트 <= 루트 노드
print()

# 부모 테이블 프린트
print(f'부모 테이블 : ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')