#00:55:31.84
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
모든 사람이 심사 받는 데 걸리는 최소시간을 구하는 문제
=> X 시간안에 M명을 처리가능 여부 문제로 바꿀 수 있기 때문에 이분 탐색 대상이 '시간'인 매개변수 탐색

1. 이분 탐색이기 때문에 최소시간 left = 1, right = 가장 빠른 심사대에서 모든 인원(M명)이 심사할 때 걸리는 시간으로 정의,
    가능한 최소 시간 후보는 answer에 저장하고, answer = right로 초기화
2. 이분 탐색의 중심 mid = (left+right)//2를 정의
3. mid 시간동안 각 심사대가 몇 명 처리할 수 있는지 계산하기 위해
    - 몇 명 처리할 수 있는지 저장할 변수 total 선언
    - for문으로 각 심사대에서 걸리는 시간을 접근해 mid//time하여 처리가능 인원수를 total에 저장
4. M 인원수보다 total이 크면 mid 시간이 충분한 것이므로 더 최솟값이 존재할 수 있으니 right = mid-1
5. M 인원수보다 total이 작으면 mid 시간이 부족한 것이므로 left = mid + 1
'''

N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

T = sorted(T)
left = 1
right =  T[0] * M # 가장 빠른 심사대에서 모든 인원이 다 심사 => 최댓값
answer = right

while left <= right:
    mid = (left + right) // 2
    # mid 시간 동안 각 심사대에서 몇명 처리 가능한지 계산
    total = 0
    for time in T:
        total += (mid // time)
    if total >= M: # 인원수보다 더 처리 가능하면
        # mid 시간 충분 => 최소시간 후보, 더 줄어들 가능성 존재
        answer = mid
        right = mid - 1
    else: # 인원수보다 더 처리 못하면
        # mid 시간 부족 => 시간 늘려야함
        left = mid + 1
print(answer)
        
    
    


