'''
input
- 첫째 줄에 식량창고의 개수 N (3<=n<=100)
- 둘째 줄에 공백을 기준으로 각 식량창고에 저장된 먹이의 개수 K ( 0<= K <= 1000)
output
- 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값 출력

예시
4
1 3 1 5

8
'''
import sys
# 식량 창고 N
N = int(input())
if not 3 <= N <= 100:
    sys.exit()

# 식량 창고에 저장된 먹이의 수
food = list(map(int, input().split()))
# for e in range(len(food)):  # 시간 줄이게 loop말고 다른 방법 없나
#     if not 0 <= food[e] <= 1000:
#         sys.exit()

# 앞에 이미 계산된 결과 저장하기위한, memoization 위한 DP table 초기화
dp = [0] * 100

# bottom up dynamic programming
dp[0] = food[0]
dp[1] = max(food[0], food[1])
for i in range(2, N):   # 앞에 두개 빼주세용
    dp[i] = max(dp[i - 1], dp[i - 2] + food[i])   # 전전 식량 창고 에서 찾는 최대 식량의 개수 + 현재 식량 정보

print(dp[N - 1])