#00:23:51.20
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
날 별로 주가를 알고있을 때 주식을 사거나 팔아서 얻을 수 있는 최대 이익 구하는 문제
- 어떤 날 주식 샀을 때, 미래의 최고점에서 파는 게 가장 최대의 이익
- 앞에서부터 순회하면 매 순간 뒤까지 훑어야하므로 O(N^2)
- 따라서, 뒤부터 주가를 탐색하면 한번 순회로 끝남 O(N)

1. 뒤에서부터 주가 탐색하기 위해 for문을 N-1부터 -1전까지 -1씩 접근하도록 작성
2. 최대 주가를 미래에서부터 갱신
    - 뒤에서부터 확인하기 때문에 최대 주가가 또 갱신되기 전까지의 이익은 profit에 max_price - prices[i]해서 저장됨
'''

T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_price = 0
    profit = 0
    
    for i in range(N - 1, -1, -1): # 미래에서 현재로 탐색
        if prices[i] > max_price: # 최대 주가 갱신
            max_price = prices[i]
        else:
            profit += max_price - prices[i]
    print(profit)