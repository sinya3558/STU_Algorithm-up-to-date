#00:26:39.78
import sys
import heapq

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
N * N 표에서 N번째 큰 수 구하는 문제
- 입력 받을 떄는 수의 크고 작음을 알 수 없기 때문에 
- 다 하나의 배열에 넣어서 최소힙 heapq를 사용
- N_arr에 모두 다 넣으면 N*N으로 메모리 초과나기 떄문에
    1. 입력받을 때마다 heappush로 힙(N_arr)에 넣어주고
    2. 힙(N_arr)의 크기가 N개 초과하면, 가장 작은 수(heap[0])는 heappop으로 제거
        => 큰 수만 N개 유지
    3. 마지막에 남은 heap의 루트 (heap[0])가 N번째로 큰 수
'''

N = int(input())
N_arr = []
for _ in range(N):
    for i in list(map(int, input().split())):
        heapq.heappush(N_arr, i)
        if len(N_arr) > N:
            heapq.heappop(N_arr)
    
print(N_arr[0])