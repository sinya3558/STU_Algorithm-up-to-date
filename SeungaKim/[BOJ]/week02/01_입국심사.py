# 7월 2주차 공통문제 
# https://www.acmicpc.net/problem/3079
# 5:41

import sys

# N = 입국심사대 개수, M = 사람수
N, M = map(int, input().split())

# N, M 인풋 제한
# if N < 1 or N > 100000:
#     sys.exit()
# if M < 1 or M > 1000000000:
#     sys.exit()
if not (1 <= N <= 100000 and 1 <= M <= 1000000000):
    sys.exit()

# 유저 인풋(N개) 받아서 T_k 값 각각 지정하기
T_k = []    # empty list
for _ in range(N):
    T_k.append(int(input()))
# print(T_k)

low = 1
high = max(T_k) * M # 최악의 케이스인 경우 -> 최고 시간 걸리는 심사대 1개, 마지막 사람 M 명 까지 모두 다 검사 할 경우

# Check base
# if high >= low:
#     mid = (high + low) // 2

min_time = 0

while high >= low:
    # BS 중간값과 입국심사 통과된 학생들 수 기본값 셋업
    mid = (high + low) // 2
    passed_M = 0

    # 지정해준 BS 중간값 사용해서 몇명의 학생들 심사대 통과하는지 반복문 이용하여 체크
    for k in T_k:
        passed_M += mid // k
        # print(passed_M)

    # 예상시간보다 더 적게 필요할 경우 BS boundary values 새로 업데이트 -> 시간 줄이기
    if passed_M >= M:
        min_time = mid
        high = mid - 1
        
    else:
        # 예상시간 초과한 경우 -> 시간 늘리기
        low = mid + 1
        #

print(min_time)
