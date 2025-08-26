#00:55:30.28
import sys
import math

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
자연수 N이 하나 이상의 연속된 소수 합으로 나타낼 수 있는 경우의 수 구하는 문제
- 소수 찾기 위해 1-N까지 배수들을 다 지워주는 방식으로 소수를 구함
- 연속된 소수 합을 구하기 위해 start, end로 연속된 소수의 양끝을 표시하도록 두포인터를 사용

1. 1 - N까지의 소수 판별
    - 배수를 제외한 모든 수가 소수이므로 소수 여부를 저장하는 배열을 선언
    - N의 제곱근까지 접근하면 되니까 for문 중첩으로 사용해 첫번쨰 for문에서 2부터 N의 제곱근까지 접근
    - 모든 i의배수 접근해 False로 바꾸기위해 두번째 for문으로 접근
2. 연속된 소수의 합 구하기
    - 연속된 소수의 합을 구하기 위해 양끝을 start, end로 표시
    - 현재 구간의 합을 저장하기위해 total 변수 사용, 합이 N이 되는 경우의 수 저장하기 위해 cnt 변수 사용
    - total >= N이면 합을 더 줄여야하니까 start +=1
    - end가 prime의 끝까지 접근하면 더 이상 늘릴 수 없으므로 종료
    - 합이 N보다 작으면 구간을 확장해야하므로 end += 1
'''

N = int(input())

is_prime = [True] * (N+1) # N까지의 소수여부 배열
is_prime[0] = is_prime[1] = False # 0,1은 소수 아님

for i in range(2, math.isqrt(N)+1):
    if is_prime[i]: # 소수인 수이면
        for j in range(i*i, N+1, i): # 그 수의 배수는 다 소수 아니니까
            is_prime[j] = False

prime = [i for i in range(N+1) if is_prime[i]]        
cnt = 0
start, end = 0, 0
total = 0

while True:
    if total >= N:
        if total == N:
            cnt += 1
        total -= prime[start]
        start += 1
    elif end == len(prime):
            break
    else:
        total += prime[end]
        end += 1
print(cnt)