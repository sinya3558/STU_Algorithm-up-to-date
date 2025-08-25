#00:55:08.40
import sys

#sys.stdin = open("input.txt",'r')

def input():
    return sys.stdin.readline().rstrip()

'''
정수 X를 3이나 2로 나누거나 1를 빼면서 1로 만드는데 연산을 사용하는 횟수의 최솟값과 계산에 포함되어있는 수를 출력하는 문제
- 6 -> 3 -> 1 => 2번
- 6 -> 2 -> 1 => 2번 이런식으로 2와 3 작은 숫자는 반복되서 계산되므로 미리 저장하면 불필요한 연산 줄일 수 있음
- 부분적인 최적해가 큰 문제의 최적해가 되므로 DP 사용.

1. 연산횟수 최솟값과 바로 전 연산 포함되어있는 수 같이 저장하기 위해 dp = {i:[min, num]}
    - dp[0] = [0,0], dp[1] = [0, 1]
2. dp 딕셔너리에 값저장하기 위해 for문으로 2부터 X까지 접근
    - 3이나 2로 나누어지는지 확인하고 -1값까지 확인해서 그 중 가장 연산횟수 작은 것 dp[i][0]에 저장
    - 가장 연산횟수 작은 수도 dp[i][-1]에 저장
3. 맞게 출력하기 위해 tmp = dp[tmp][-1]로 계속 접근해 출력
'''

X = int(input())

# dp = {i :[min, num]} : i를 1로 만드는 연산횟수 최솟값과 바로 전 연산에 포함되어있는 수
# dp[0] = [0, 0], dp[1] = [0, 1]}
dp = {i:[0, 0] for i in range(X + 1)}
for i in range(2, X+1):
    n_3, n_2, n_minus = [1e7, 0], [1e7, 0], [1e7, 0] 
    if i % 3 == 0:
        n_3[0] = dp[i // 3][0] + 1
        n_3[-1] = i // 3
    if i % 2 == 0:
        n_2[0] = dp[i // 2][0] + 1
        n_2[-1] = i // 2
    n_minus[0] = dp[i - 1][0] + 1
    n_minus[-1] = i - 1
    
    dp[i][0] = min(n_3[0], n_2[0], n_minus[0])
    
    if min(n_3[0], n_2[0], n_minus[0]) == n_3[0]:
        dp[i][-1] = n_3[-1]
    elif min(n_3[0], n_2[0], n_minus[0]) == n_2[0]:
        dp[i][-1] = n_2[-1]
    else:
        dp[i][-1] = n_minus[-1]

print(dp[X][0])
tmp = X
print(X, end = ' ')
while tmp > 1:
    print(dp[tmp][-1], end = ' ')
    tmp = dp[tmp][-1]
print()