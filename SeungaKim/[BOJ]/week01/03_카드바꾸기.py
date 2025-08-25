# 공통문제 레벨 : 실버 3이상
# https://www.acmicpc.net/problem/25401
# 1:17
'''
입력 1 
4
1 2 2 4

출력 1 
1
(1 2 3 4)

입력 2 
5
6 3 3 1 -1

출력 2 
2 
(7 5 3 1 -1)
'''
import sys

N = int(input())

if not 2 <= N <= 500:
    sys.exit()  # out of range (N)

deck = list(map(int, input().split()))  # 유저 인풋값 넣은다음

for x_i in deck: 
    if not -1000000 <= x_i <= 1000000:
        sys.exit()  # out of range (user input)

''' 조건 : 
    (1) 규칙적으로 증가: +d
    (2) 감소 : -d
    (3) 일정: d = 0 
    => 최소 변화로 카드덱 등차수열 만들어 버리기 '''

min_flip_nums = N
d = 0
# time error 왜 나는거지
for i in range(N): # 기준점 카드(a_1)
    count_d = {}    # 동일한 공차의 개수 카운트를 위ㅎ나 딕셔너리 *** {-2 : 3번, 0 : 1 번, 3: 1번...etc}
    for j in range(N):  # *** for j in range(1, N) 하는 경우, j 인덱스 0 은 무시하고 넘어감. **
        if i == j :     # 동일 인덱스 i,j 는 피한다
            continue    
        value_diff = deck[j] - deck[i]
        idx_diff = j - i

        if (value_diff) % (idx_diff) != 0:  # d 값이 정수로 떨어지는거 아니면 넘긴다
            continue
        d = (value_diff) // (idx_diff)

        # count_d = {}    # 동일한 공차의 개수 카운트를 위ㅎ나 딕셔너리 
        # defaultdict?
        if d in count_d:
            count_d[d] += 1 # update
        else:
            count_d[d] = 1  # init 

# 기준점 카드 i 포함 → 길이: count + 1 (카드 두 쌍이 하나로 ㅋ카운트)
    if count_d:
        max_count = max(count_d.values())
    else:
        max_count = 0   # empty dictionary 인 경우
    actual_change = N - (max_count + 1)
    min_flip_nums = min(min_flip_nums, actual_change)

# 아.. 카드 정렬 필요없는거...
print(min_flip_nums)


# 5:29