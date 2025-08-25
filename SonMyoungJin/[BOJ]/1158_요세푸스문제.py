#00:27:52.17
import sys
from collections import deque

#sys.stdin = (open("input.txt",'r'))

'''
N명의 원형 배열에서 K번째 사람을 지속적으로 제거하는 문제
1. 원형 배열 구현하기 위해서 큐를 사용
2. 큐에서 K번째 사람 제거
    - 앞에서 K번째 사람을 제거하려면, 큐는 원형 구조이므로 큐에서 앞의 사람을 K-1번 회전시켜야함
    - 왼쪽으로 회전해야하므로 queue.rotate(-(K-1))
        f 1234567 => f 2345671 => f 3456712
        큐에서 3번째 사람 제거하기 위해 2번 회전
'''

N, K = list(map(int, sys.stdin.readline().strip().split()))


people = []
result = []

# 사람들 리스트를 큐로 변환
# queue = deque([i for i in range(1, N+1)])
for i in range(N):
    people.append(i+1)
queue = deque(people)

#큐가 빌때까지 제거해야하므로 while queue:
while queue:
    # k-1번째를 큐에서 pop하여 맨뒤로 보내기 위해 
    queue.rotate(-(K-1))
    # K번째 사람을 pop하고 결과 리스트에 추가
    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>") 