# 각 노드가 연결된 데이터 표현하는 graph, 2d list
graph = [
[],         # 보통 1번 노드부터 시작이라-> 0번 노드는 empty 로 초기화 시킴
[2, 3, 8],
[1, 7],
[1, 4, 5],
[3, 5],
[3, 4],
[7],
[2, 6, 8],
[1, 7]
]

# 처음엔 각 노드 방문 없음으로 초기화
visited = [False]*9

# 큐 자료구조라서 -> collections 안에 deque 라이브러리 필수
from collections import deque

# BFS
def bfs(graph, start, visited):
	# Queue 구현을 위해 deque 라이브러리 사용
	q = deque([start])
	# 현재 노드를 방문처리 해버렷
	visited[start] = True
	
	# 큐가 빌때까지 반복
	while q:
		# 큐에서 하나의 원소를 뽑아 출력하기
		v = q.popleft()   # 가장 밑바닥 뽑아내기. FIFO
		print(v, end=' ')
		# 아직 방문하지 않은 인접한 원소들을 전!부! 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				q.append(i)
				visited[i] = True

bfs(graph, 1, visited)