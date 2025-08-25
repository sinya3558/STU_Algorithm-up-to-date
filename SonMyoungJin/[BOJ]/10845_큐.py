#00:20:45.65
from collections import deque
import sys

#sys.stdin = open("input.txt",'r')

'''
정수를 저장하는 큐(FIFO)룰 구현하고 명령 처리
- 양방향 큐 deque() 사용
    - pop은 popleft() 시간복잡도 O(1)
    - queue를 list로 구현하면 pop(0) 시간복잡도 O(n)
        앞에 있는 원소 삭제할 때마다 한 칸씩 이동해야 하기 때문에
- push는 append()
- size는 len(), front와 back은 인덱스로 접근
'''

N = int(sys.stdin.readline().strip())
queue = deque()

for _ in range(N):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) == 2: #push element
        queue.append(int(cmd[-1]))
    else:
        if cmd[0] == 'pop':
            print(queue.popleft() if queue else -1)
        elif cmd[0] =='size':
            print(len(queue))
        elif cmd[0] == 'empty':
            print(0 if queue else 1)
        elif cmd[0] == 'front':
            print(queue[0] if queue else -1)
        elif cmd[0] == 'back':
            print(queue[-1] if queue else -1)