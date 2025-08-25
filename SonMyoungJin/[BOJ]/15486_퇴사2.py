#01:13:04.50
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
퇴사일(N+1)전까지 상담에 걸리는 기간 T와 받을 수 있는 금액 P를 고려한 최대 이익을 구하는 문제
- 각 날짜마다의 최대이익을 점진적으로 구해나가야하기 때문에 DP사용.
1. i일까지의 얻을 수 있는 최대이익을 저장하기 위해 dp배열 사용.
    - 퇴사일은 N+1일이므로 N일까지의 최대이익을 저장하기 위해 dp = [0] * (N+1)
'''

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

#dp[i] : i일까지 상담진행한 후 얻을 수 있는 최대 이익
dp = [0] * (N+1)
for i in range(N): 
    dp[i + 1] = max(dp[i + 1], dp[i]) # 상담 아직 안함, 이전날짜까지의 최대 이익
    if i + T[i] <= N: # 상담완료기간이 퇴사일보다 전이면 상담 가능
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])
#print(dp)
print(dp[N]) # 퇴사일까지 얻을 수 있는 최대 이익 출력