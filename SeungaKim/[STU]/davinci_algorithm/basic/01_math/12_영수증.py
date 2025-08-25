# https://www.acmicpc.net/problem/25304
'''
input:
첫째 줄에는 영수증에 적힌 총 금액 
X가 주어진다.

둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
N이 주어진다.

이후 N개의 줄에는 각 물건의 가격 
a와 개수 b가 공백을 사이에 두고 주어진다.

output:
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No
'''
# 9:31
# input() 대신 readline() 써보기
import sys

# X = total amount of payment, N = nums of product that purchased
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
# constraint 1
if not 1 <= X <= 1000000000 or not 1 <= N <= 100:
    sys.exit()

total_price = 0
for _ in range(N):
    price, cnt = map(int, sys.stdin.readline().split())
    # constraint 2
    if not 1 <= price <= 1000000 or not 1 <= cnt <= 10:
        sys.exit()
    total_price += price * cnt

# if total_price == X:
#     print("Yes")
# else:
#     print("No")
print("Yes" if total_price == X else "No")