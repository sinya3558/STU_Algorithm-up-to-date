#01:09:42.52
import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
한 도시에서 출발하여 도달할 수 있는 도시 중 최단거리가 K인 도시를 출력하는 문제
- 한 정점에서 다른 모든 정점까지의 최단거리 구하는 문제
- 간선 가중치가 양수
=> 다익스트라 (우선순위 큐 + 최소힙 사용)
BFS => 가중치 1인 다익스트라
1. 각 정점까지는 도달할 때의 최단거리가 계속 계산될테니까 DP배열로 저장
    - short_path[i] = [-1] * (N + 1)
    - -1로 초기화
2. 각 도시와 출발지부터 그 도시까지의 최단거리를 저장해야하므로 큐를 선언하는데 (현재 도시, 최단거리)를 push
    - 방문안했으면(-1이면) 거리+1하고 큐에 넣어서 접근
'''

N, M, K, X = map(int, input().split())
Map = {i:[] for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    Map[A].append(B)

# short_path[i] : X로부터 출발하여 i까지 도달할 수 있는 최단 거리
short_path = [-1] * (N + 1)
short_path[X] = 0

queue = deque([(X, 0)])

while queue:
    cur, dist = queue.popleft()
    for next in Map[cur]:
        if short_path[next] == -1:
            short_path[next] = dist + 1
            queue.append((next, dist + 1))

found = False
for i in range(N+1):
    if short_path[i] == K:
        print(i)
        found = True
if not found:
    print(-1)