# https://www.acmicpc.net/problem/2075
# 04:45PM
# 1. 문제 설명
"""
NxN 표에 정수 N^2 개가 있다. 모든 수는 자신의 한 칸 위에 있는 수보다 크다 / (인접 노드(상))
표에 채워진 수는 모두 다르다 / identical
N 번째 큰 수를 찾는 프로그램을 작성하시오

INPUT:
N 그 다음 라인부터 N^2 개의 수가 띄어쓰기로 들어온다
[ex. input]
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49

OUTPUT:
N번째 큰 수를 출력한다
[ex. output]
35
"""
# 2. 문제 해결 아이디어
'''
각 노드 위치에서 인접한 노드(바로 위)데이터 값보다 무조건 큰 데이터가 입력된다
row는 몰라도 col 에서는 ascending order.
이 상황에서 N 번째로 큰 수를 찾기만 하고 sorting 필요 없으면... heapq 써야하남요?
'''
# 3. 몰랐던 것
'''
heapq.heappush() 쓸 때, iterable 한 단일 요소만 넣어야함. list 통으로 넣음 안됨 바보야
'''
# 4. 
import heapq

# User input, N
N = int(input())
# user input, N^2 numbers
nums = []
# heapq.heapify(nums) #  nums 이제 힙이 됨

for _ in range(N):
    # rows = map(int, input().split())
    for row_ele in map(int, input().split()):   # row_ele = element in row
        if len(nums) < N:
            heapq.heappush(nums, row_ele)  # 유저 입력값 힙 nums 에 추가
        else:
            if row_ele > nums[0]:
                heapq.heappushpop(nums, row_ele)

# heapq.nlargest(N, nums)    # 가장 큰 요소 N 개를 리스트로 반환
# print(nums)             
print(nums[0])              # 그 중 제일 작은거 -> N번째 큰 수 
# 5:26