# dynamic programming exercise
# 아이디어 생각하기가 어렵네
'''
N 가지의 화폐가 있다. 
화페의 계수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 할 때, 사용되는 최소한의 화폐 개수를 출력해라

EX.
2원, 3원 N=2개의 화폐가 있을 때,
M=15원을 만들기 위한 최소한의 동전 사용은 
3원 * 5 = 15

5를 출력한다
'''

'''
입력
- 첫째 줄에 N, M (1 <=N<= 100, 1<= M <= 10000)
- 이후의 N 개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는  10000 보다 작거나 같은 자연수

출력
- 첫째 줄에 최소 화폐 개수를 출력한다, 불가능 하면 -1

EX.
input 
3 7
2 3 5

2
'''
# c = [2 3 5] 일때, 2, 3, 5 화폐 추가해가면서 하나씩 다 확인 -> 그리고서 min 값으로 update(갱신)

# user input N, M
N, M = map(int, input().split())

# user input - list of coin
c_list = list(map(int, input().split()))
# print(c_list)

# 중복 계산 피해주기 -> set up DP table
dp = [10001] * (M + 1)  # 10001 == INF (since 1 <= M <= 10000, 1원 10000 개가 맥시멈 )

# dynamic programming - bottom-up
dp[0] = 0   # 0원은 0으로 init
for i in range(N):      # [2, 3, 5] -> i
    for j in range(c_list[i], M + 1):   # [2,..., 8], [3,...,8],[5,...,8] -> j = idx of M in [0,8]
        # i = 2, 3, 5 확인하고 j = 목표 금액 M 이하 범위 인덱스(금액 i로 만들기 가능하면, INF -> 동전 개수로 덮어씌운다) 
        if dp[j - c_list[i]] != 10001 :
            dp[j] = min(dp[j], dp[j - c_list[i]] + 1)   # 최소 동전수 갱신하면 바꿔주기

if dp[M] == 10001 : # INF 일때(=그니까 동전 조합이 불가능일 때),
    print(-1)
else:
    print(dp[M])    # 아 바보야 dp[j] 가 말이되냐