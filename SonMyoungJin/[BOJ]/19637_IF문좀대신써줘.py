#00:58:39.62
import sys

#sys.stdin = open('input.txt','r')
'''
M개의 캐릭터 전투력에 대해서 전투력 상한값 기준으로 맞는 칭호를 찾아내는 문제
1. power <= 10000이면 WEAK 이기 때문에 캐릭터의 전투력이 포함될 수 있는 가장 작은 상한값을 가진 칭호 찾아야함.
    - 따라서, binary search 사용
    - M개의 전투력에 대해서 각각 칭호(N개)를 binary search 하면 O(MlogN)
'''
N, M = map(int, sys.stdin.readline().split())

# 전투력 상한값과 그 기준에 따른 칭호 정보
powers = []
for _ in range(N):
    tmp = sys.stdin.readline().split()
    powers.append((int(tmp[-1]),tmp[0])) # (상한값, 칭호 이름)

#캐릭터 전투력 정보  
chr_powers = [int(sys.stdin.readline()) for _ in range(M)]

# 칭호 리스트를 binary search
# 해당 전투력에 대해 가장 작은 상한값을 가진 칭호 search
def binary_search(powers, c_p):
    left, right = 0, len(powers) - 1
    while left <= right:
        mid = (left + right) // 2
        if powers[mid][0] >= c_p: # 전투력에 해당하는 칭호 찾았으면
            right = mid - 1         # 더 작은 값 있을수도 있으니까 왼쪽 절반 탐색
        else:
            left = mid + 1          # 전투력에 맞지 않으면 오른쪽 절반 탐색
    # 시작점이니까 가장 작은 상한값을 가진 칭호의 인덱스
    # c_p 보다 작거나 같은 가장 큰값의 인덱스
    return left

for c_p in chr_powers:
    idx = binary_search(powers, c_p)
    print(powers[idx][-1])