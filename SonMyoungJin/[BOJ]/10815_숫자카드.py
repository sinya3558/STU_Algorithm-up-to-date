#00:32:15.33
import sys

#sys.stdin = open('input.txt','r')

'''
M개의 정수에 대해 N개의 숫자카드 확인해 해당 정수있는지 없는지 확인하는 문제
선형 탐색 : O(N) => O(N + M * N) 시간 초과!
이분 탐색 : O(logN)
            - 처음 sort O(NlogN)
            - 쿼리마다 이분 탐색 O(MlogN)
            => O(NlogN + MlogN)
따라서, 이분 탐색 사용.
    - 정렬된 배열의 중간값 찾기
    - left, right 인덱스로 값에 접근해 중간값과 비교
        - 중간값보다 target이 크면 left = mid+1로 오른쪽 절반 탐색
        - 중간값보다 target이 작으면 right = mid+1로 왼쪽 절반 탐색   
'''

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

cards.sort()
result = []

def binary_search(cards, num):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == num:
            return True
        elif cards[mid] < num: # 중간값이 target보다 작으면 오른쪽 절반 탐색
            left = mid + 1
        else:                  # 중간값이 target보다 크면 왼쪽 절반 탐색
            right = mid - 1
    return False

for query in queries:
    if binary_search(cards, query):
        result.append('1')
    else:
        result.append('0')

print(" ".join(result))

'''
# cards를 set으로 하고 선형탐색하면 시간초과 안남.
# set의 검색시간은 O(1) => 메모리는 좀 더 차지함.
# N개의 숫자를 set으로 생성 => O(N)
# M개의 쿼리에 대해 각 쿼리가 set에 있는지 확인 => O(M)
# 전체 시간복잡도 : O(N+M)

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

result = []

for query in queries:
    if query in cards: # cards가 set이라서 O(1)
        result.append('1')
    else:
        result.append('0')
print(" ".join(result))
'''
