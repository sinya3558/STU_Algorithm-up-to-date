#00:43:12.57
import sys
from collections import deque

#sys.stdin = open("input.txt", 'r')

'''
프린터에서 중요도 높은 문서 먼저 출력
- 먼저 요청된 문서부터 순차적으로 처리하므로 deque 사용
    삽입, 삭제연산 O(1)
- 우선순위 비교와 인쇄 순서 접근을 위해 각 문서를 (priorities, idx)형태로 큐에 저장
- 현재 문서보다 하나라도 우선순위 높은게 있으면 현재 문서를 큐의 뒤로 보내기 위해 any() 사용
    O(N^2)이긴 하지만 0 < N <= 100 이기 떄문에 처리 가능
    max()를 쓰면 O(N^2)로 똑같지만, 큐 비었는지 확인 과정이 추가적으로 필요 
- 인쇄 순서를 추적하기 위해 order 변수 선언
'''

T = int(sys.stdin.readline().strip())
for _ in range(T):
    # N: 문서의 개수, M: 궁금한 문서 인덱스
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    
    # 문서의 중요도 입력받음
    priorities = list(map(int, sys.stdin.readline().strip().split()))
    
    # (중요도, 인덱스) 형태로 deque에 저장
    queue = deque()
    for idx, priorities in enumerate(priorities):
        queue.append((priorities, idx))
    
    # 문서 인쇄 순서
    order = 0 
    
    # 큐 비어있지 않으면(출력을 기다리는 문서 있으면) 계속 처리
    while queue:
        # 문서 하나 꺼냄
        cur = queue.popleft()
        #큐에 다른 문서들 중 하나라도 현재 문서보다 우선순위가 더 높으면, 현재 문서를 뒤로 보냄
        if any(cur[0] < doc[0] for doc in queue):
            queue.append(cur)
        else:
            # 우선순위 가장 높은 문서 출력, 인쇄 순서 증가
            order += 1
            # 현재 인쇄된 문서가 궁금한 문서면 인쇄 순서 출력
            if cur[-1] == M:
                print(order)
                break
    