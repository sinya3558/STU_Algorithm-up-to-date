#01:12:00.00
import sys

#sys.stdin = open('input.txt','r')

'''
코드 참고: https://talktato.tistory.com/69

모든 도시 방문하고 다시 시작 도시로 돌아오는 최소 비용 구하는 문제
이동할 수 없는 경로나 최소 비용을 이미 넘어가는 경로는 중단 하는 것이 효율적 => 백트래킹 사용

1. 최소 cost를 비교하며 찾기 위해 min_cost 변수를 1e7로 초기화. (1e6+1은 틀렸습니다 나옴)
2. 도시를 순회(백트래킹)
- 모든 도시를 순회했는지 확인하기위해 visited에 False 있는지 확인
    - 현재 최소 비용보다 더 작다면 최소 비용 갱신
- 모든 도시 효율적으로 순회하기 위해
    - 경로 있는지, 방문한 적은 없는지, 현재 비용이 최소 비용을 넘었는지 확인(맞지 않으면 가지치기)
    - 순회 가능하다면 방문 표시(visited[i] = True)
    - DFS 재귀호출하여 순회
    - DFS 함수 호출 끝났을 때,
        - 모든 도시 순회했다면 return min_cost 일거고
        - 그 다음 도시 순회할 수 있으면 계속 재귀호출 일거고
        - 그 다음 도시 순회 못한다면 현재 도시에서 다른 도시 방문해야하므로 방문 표시를 해제
3. 출발점이 정해져있지 않기 때문에 모든 도시를 출발점으로 시도.
'''
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# 모든 weight가 1000,000이하 이므로 1e7로 초기화. 
min_cost = 1e7

def DFS(start, next_city, visited, cost):
    global min_cost
    
    # 모든 도시를 순회했는지 확인
    if False not in visited:
        # 마지막 도시에서 시작 도시로 돌아올 수 있어야하니까 확인
        if W[next_city][start] > 0:
            min_cost = min(min_cost, cost + W[next_city][start]) # 최소 비용 갱신
        return min_cost
    
    # 모든 도시를 아직 순회하지 않았다면
    for i in range(N): # 다음 도시 선택
        if (W[next_city][i] > 0) and (not visited[i]) and (cost < min_cost):
            visited[i] = True # 해당 도시 방문 표시
            DFS(start, i, visited, cost + W[next_city][i]) # 그 도시 이동하여 DFS 탐색
            visited[i] = False # 해당 도시를 다시 방문하지 않도록 표시 해제
            
# 출발지 정해져 있지 않으니까 모든 도시로 시작하는 방법을 모두 순회
# 방문 여부 기록하기 위해 visited 배열 요소 모두 False로 초기화
for i in range(N):
    visited = [False] * N
    visited[i] = True # 현재 도시를 출발 도시로 True, 방문 처리
    DFS(i, i, visited, 0)
print(min_cost)