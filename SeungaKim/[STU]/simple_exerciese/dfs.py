graph = [

[],           # 보통 1번 노드부터 시작하기 때문에, 0번은 Empty 로 초기화시켜둠
[2, 3, 8],
[1, 7],
[1, 4, 5],
[3, 5],
[3, 4],
[7],
[2, 6, 8],
[1, 7]

]

# 처음엔 9개의 노드 모두 방문하지 않은 것으로 표시 ( 1d list)
visited = [False]*9

# DFS method definition
def dfs(graph, v, visited):
	# 현재 노드 방문 처리
	visited[v] = True
	print(v, end=' ' )
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
			
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)  # 0 아니고 노드 1 부터 방문체크