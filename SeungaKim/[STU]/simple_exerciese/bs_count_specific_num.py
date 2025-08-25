# binary search : counting nums of specific data from sorted list
'''
input
7 2
1 1 2 2 2 2 3

output
4

첫째 줄 N (arr 안 데이터 수), X (개수 카운팅 하고 싶은 데이터)
두번째 줄 N 개의 정수 띄어쓰기로 입력

출력 : 원소 중 값이 X 인 데이터의 개수 출력. 하나도 없으면 -1
'''
# 잉 이거 어디선가 봤는데 왜 익숙하지
# 특정값 -> 첫번째 위치와 마지막 위치 차이 계산
from bisect import bisect_left, bisect_right

# function that returns numbers of data in [left_val, right_val] 
def count_data(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx

N, X = map(int, input().split())
list_num = list(map(int, input().split()))

# cnt = count_data(list_num, 0, N - 1)
cnt = count_data(list_num, X, X) # 아이고 바보야. 문제 좀 기억해!

if cnt == 0:
    print(-1)
else:
    print(cnt)