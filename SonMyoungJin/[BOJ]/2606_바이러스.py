#00:29:03.63
import sys
from collections import deque

#sys.stdin = open("input.txt",'r')

'''
바이러스 전파된 컴퓨터 수 구하는 문제

- 네트워크 상에서 연결된 모든 컴퓨터를 찾아야 하기 때문에, 바이러스 전파 과정을 자연스럽게 시뮬레이션할 수 있는
(현재 노드와 직접 연결된 모든 노드를 우선적으로 방문하는) BFS를 사용.
- 각 컴퓨터마다 연결된 컴퓨터의 번호가 주어지므로 graph라는 변수를 dict으로 선언하여, 연결상태를 표현.
- BFS에서 방문할 노드에 바로 접근하기 위해 FIFO인 deque 자료구조 사용
- 이미 감염된 컴퓨터를 체크하기 위해 중복을 막는 set구조를 spead 변수로 선언.

'''
# N: 컴퓨터 수, M = 간선(연결) 수
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 컴퓨터 별로 연결된 컴퓨터들을 저장할 dict인 변수 graph 초기화
# key : 컴퓨터 번호(1~N), value : 연결된 컴퓨터 list
graph = {(i+1) : [] for i in range(N)}

# 연결 수가 M개 이므로 for문으로 반복해서 정보 받음
for _ in range(M):
    key, value = list(map(int, sys.stdin.readline().strip().split()))
    # 양방향 연결 일테니까 양쪽 모두에 추가
    graph[key].append(value)
    graph[value].append(key)

def BFS(start_node):
    # BFS를 위한 큐 생성 및 시작 노드 추가
    queue = deque([start_node])
    # set을 사용해 중복 방지
    spread = set([start_node])
    
    while queue:
        curr_node = queue.popleft()
        for next_node in graph[curr_node]:
            # 감염되지 않았다면
            if next_node not in spread:
                # 감염 표시하고 다음 연결된 노드 처리 위해 큐에 추가
                spread.add(next_node)
                queue.append(next_node)
    # 감염된 컴퓨터 수 세기 위해 spread return
    return spread
# 1번 컴퓨터 자신은 제외해야하므로 len(spread)-1
print(len(BFS(1))-1)

            


