# https://www.acmicpc.net/problem/11501
# 11:24
'''
매일매일 3 중 1 택
1. 주식 하나 산다
2. 원하는 만큼 가지고 있는 주식을 판다
3. 아무것도 안한다

최대 이익을 계산하는 프로그램
10 7 6 -> 최대 이익 : 0
3 5 9 -> 최대 이익 : 10 (8 아니고?)

INPUT
num of test cases : T
days of test case 1 : N (2 <= N <= 1000000)
stock * N by split()
days of test case 2 : N
stock * N
..

OUTPUT <- 답은 부호있는 64bit 정수형으로 표현 가능하다.
max.profit(case1)
max.profit(case2)
..
'''
# 근데 나 프로핏 계산 모르겠는데..?
# => 가장 비싼 날까지 주식 1 주씩 모아두고 한꺼번에 팔면 최대 이익
import sys

user_input = sys.stdin.readline

T = int(user_input())

for _ in range(T):
    N = int(user_input())
    if not 2 <= N <= 1000000:
        sys.exit()

    stocks = list(map(int, user_input().strip().split()))   # strip() :  줄바꿈'\n 제거
    if any(s > 10000 for s in stocks):
            sys.exit()

    best_profit = 0
    max_stock = 0
    # cnt_day = 0
    for s in reversed(stocks):
        # max_stock = max(stocks)
        if s > max_stock:   # 크면
            max_stock = s
            # cnt_day += 1
        else :
            best_profit += max_stock - s

    print(best_profit)

    # runtype error 왜.. EOF error// time complexity 자꾸 (****)
#1:07