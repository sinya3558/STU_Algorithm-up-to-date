#00:21:44.68
import sys
import heapq

#sys.stdin = open("input.txt", 'r')

'''
최대 힙을 구현하기 위해 heapq 모듈 사용하는데,
해당 모듈은 최소 힙이니까 입력 x를 음수로 바꾸어서 push
- heapq.heappush()와 heapq.heappop()의 시간 복잡도는 O(logN)
'''

N = int(sys.stdin.readline().strip())

#최대 힙 구현하기 위한 리스트 선언
max_heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        # max_heap 안의 요소 있으면 최대값 제거하고 출력
        if max_heap:
            max_num = heapq.heappop(max_heap)
            print(-max_num)
        else:
            print(0)
    else:
        # 자연수 x 삽입
        heapq.heappush(max_heap, -x)