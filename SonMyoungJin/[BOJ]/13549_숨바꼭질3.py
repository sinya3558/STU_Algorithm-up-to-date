#01:23:54.28
import sys
from collections import deque

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드 참고 : https://github.com/tony9402/algorithm-solutions/blob/main/solutions/baekjoon/13549/main.cpp

수빈 위치 N, 동생위치 K, 수빈은 X+1(1초), X-1(1초), 2*X(0초)로 움직일 수 있을 때 N에서 K까지 가는 최단 시간 구하는 문제
    - +1, -1, *2를 모두 계산해봐야 되기 때문에 BFS로 탐색
    - *2가 0초로 시간이 덜 들기 때문에, 먼저 탐색해야 최단시간을 보장
1. BFS로 탐색하기 위해 queue를 선언하고 최단시간을 저장하고 방문여부를 확인하기 위해 table배열을 문제의 최댓값까지만 포함하도록 선언
2. 시작위치 N를 queue에 넣고 시작
3. *2를 먼저 탐색하기 위해 queue 앞에 추가하기 위해 appendleft
4. +1, -1은 queue 뒤에 추가하기위해 append
'''

N, K = map(int, input().split())

MAX = 100001
table = [-1] * MAX # 최단 시간(초) 저장, -1로 초기화
table[N] = 0 # 시작 위치 0초
   
queue = deque([N]) # 수빈 자리에서 시작

while queue:
    cur = queue.popleft()
    if cur == K:
        break
    
    # 순간이동: 0초, queue 앞에 추가 => 시간 덜드는 경로를 먼저 탐색해야 최단 시간 보장
    next = cur * 2
    if 0 <= next < MAX and table[next] == -1:
        table[next] = table[cur]
        queue.appendleft(next)
    # 걷기: 1초, queue 뒤에 추가
    for next in [cur - 1, cur + 1]:
        if 0 <= next < MAX and table[next] == -1:
            table[next] = table[cur] + 1
            queue.append(next)
            
print(table[K])           
        
            



    