'''
- N 명의 병사가 무작위로 나열, 각 병사는 특정한 값의 전투력 보유
- 병사들 배치할 때 전투력이 높은 순으로 배열시킨다
- 특정한 위치에 잇는 병사는 열외시킨다. 그러면서도 남아 있는 병사의 수가 최대가 되도록 만드는 **열외 병사의 수**를 출력해라

input
- 첫째 줄에 N (1 <= N <= 2000)
- 둘째 줄에 각 병사의 전투력 입력 (0 <= power <= 10000000)
output
- 남아있는 병사가 최대가 되도록 하기 위해 열외시켜야 하는 병사의 수

i.e. input & output
case 1:
        7
        15 11 4 8 5 2 4

        2
--------------------
case 2:
        7
        4 2 5 8 4 11 15

        5
'''
import sys
N = int(input())
if not 1 <= N <= 2000:
    sys.exit()
soldier = list(map(int, input().split()))
# 여기서 전투력 확인하지말고 for loop 안에서 해볼 것

# cnt = 0
# for i in range(N - 1):  # 두개씩 비교하니까
#     if not 1<= soldier[i] <= 10000000:
#         sys.exit()
#     if soldier[i] < soldier[i + 1]:
#         # cnt.append(i)
#         cnt += 1
# print(cnt)

'''
NOTE: Longest Increasing Subsequence: 가장 긴 증가하는 부분수열..? 그니까 lognest ascending list 찾기?
- D[i] = array[i] 를 마지막 원소로 가지는 부분 수열의 최대 길이
- 모든 0 <= j < i 에 대해, D[i] = max(D[i], D[j] + 1) if array[j] < arra[i]
- LIS 부분수열의 최대 길이를 찾는다

[4, 3, 5, 8, 4, 11, 15]
-----------------------
[1, 1, 1, 1, 1,  1,  1] -> i = 0
[1, 1, 1, 1, 1,  1,  1] -> i = 1
[1, 1, 2, 1, 1,  1,  1] -> i = 2 # D[j] + 1 = 2 = D[2], 아항 그러니까 j 가 앞의 병사들 파워
[1, 1, 2, 3, 1,  1,  1] -> i = 3 # D[j] + 1 = 3 = D[3] -> 현재 파워(i) 가 앞의 파워(j) 보다 큰 경우만 업데이트
[1, 1, 2, 3, 2,  1,  1] -> i = 4 # j=1 에서 업데이트
[1, 1, 2, 3, 2,  4,  1] -> i = 5 # j=0,1,2,3,4 에서 업데이트 중 max
[1, 1, 2, 3, 2,  4,  5] -> i = 6 # j=5
'''
# 순서 뒤집어서 LIS 문제로 변환
soldier.reverse()

# init dp table
dp = [1] * N

# LIS
for i in range(N):
    if not 1<= soldier[i] <= 10000000:
        sys.exit()
    # 범위 통과하면,
    for i in range(1, N):       # 두개씩 비교해서 i=1부터 진행
        for j in range(0, i):   # i 이전 병사들과 비교
            if soldier[j] < soldier[i]:
                dp[i] = max(dp[i], dp[j] + 1)   # 조건 만족하면, 증가시켜서 업데이트

# print(dp)
# 열외시켜야 하는 병사들의 수
print(N - max(dp))