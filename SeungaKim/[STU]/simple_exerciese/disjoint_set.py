# disjoint set data structure

# user input : num of nodes and edges
n, e = map(int, input().split())
parent = [0] * (n + 1)  # 일단 부모 테이블 만들고
# 부모노드 자기 자신으로 이니셜라이즈
for i in range(1, n + 1):   # 노드 1 부터 시작
    parent[i] = i

# FUNCTIONS
# 통상적으로 원소의 루트 노드를 찾을 때 사용하는 함수명은 'find_parent'라고 짓는다
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드(부모)를 찾을 때까지 재귀 호출
    if parent[x] != x:  # 초기 테이블 이니셜라이즈할때 자기자신 지정해줘서
        return find_parent(parent, parent[x])
    # otherwise
    return x

# 두 원소가 속한 집합을 합치기 -> union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a # 더 작은 값으로 갱신하니까
    # 아니면,
    else:
        parent[a] = b

# Union operator
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# Print elements of set
print(f'각 원소가 속한 집합 = ', end='')
for i in range(1, n + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력시키기
print(f'부모 테이블: ', end='')
for i in range(1, n + 1):
    print(parent[i], end=' ')
