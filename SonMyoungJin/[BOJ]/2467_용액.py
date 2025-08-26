#00:30:34.06
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
N개의 용액이 오름차순 일 때, 서로 다른 두 개의 용액 더한 합이 0에 가까운 조합 찾는 문제
- 배열이 오름차순 정렬되어있기 때문에 양끝에서 하나씩 움직이면서 최적해를 찾도록 이분 탐색사용

1. 배열의 인덱스에 접근할 수 있도록 왼쪽 끝 ㅣ = 0, 오른쪽 끝 r = N-1으로 두 포인터를 저장
2. 최솟값을 저장하기 위해 min_sum 선언하고 범위에 따라 나올 수 있는 최댓값을 저장
3. 두 포인터에 해당하는 배열 값의 합(total)을 계산하고, 0에 가까운 값은 절댓값이므로 abs(total)과 최솟값 min_sum을 비교
4. 비교한 값은 마지막에 출력하기 위해 ans 변수에 저장
    - total이 0이면 0에 가장 가까우므로 더이상 진행할 필요없이 break
    - total > 0이면 합을 줄여야 0과 가까워지니까 큰 쪽에서 하나 내려가야하므로 r -= 1
    - total < 0이면 합을 늘려야 0과 가까워지니까 작은 쪽에서 하나 내려가야하므로 l += 1
'''

N = int(input())
solutions = list(map(int, input().split()))

l, r = 0, N - 1
min_sum = int(1e9) * 2 + 1 #float('inf')
ans = (0, 0)

while l < r:
    total = solutions[l] + solutions[r]
    
    if abs(total) < min_sum:
        min_sum = abs(total)
        ans = (solutions[l], solutions[r])
    
    if total == 0:
        break
    elif total > 0:
        r -= 1
    else:
        l += 1

print(ans[0], ans[-1])
