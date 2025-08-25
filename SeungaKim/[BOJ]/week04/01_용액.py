# https://www.acmicpc.net/problem/2467
# 11:49
'''
두 용액을 혼합해서 특성값이 0에 가장 가까운 용액을 만들려고 한다
[-99, -2, -1, 4, 98] 인 정렬된 순서인 경우,
-99 와 98 을 혼합하면 특성값이 -1인 용액을 만들 수 있다.
서로 다른 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾아 출력하라

input
첫째 줄  N (전채 용액의 수) (2<= N <= 100000)
두번째 줄 LIST ( 용액의 특성값 데이터 + 빈칸)

output
출력해야하는 두 용액의 특성값(데이터)를 ascending order 
! 두 쌍 이상인 경우는 그 중 아무거나 1
'''
# 1. 해결 아이디어
'''
- 정렬된 순서의 리스트 -> bs
- 산성 + / 알칼리 - -> 중간값 0 으로 잡고 하나씩 sum 값 비교해보면 안되나
(-99, 4)    (-2, 4)     (-1, 4)
(-99, 98)   (-2, 98)    (-1, 98)    요걸 어떻게 한담..? 이거 사실 combination 문제 아님...?
- sum(left_val, right_val) -> mininum 값 출력
- 씁 되려나
'''
# 12:12
# 14:06
# user input
N = int(input())
list_N = list(map(int, input().split()))
# print(N, list_N)

# [Method 1] 내맘대로 bs -> 시간 초과 남 XX. bc nested for loop
# # divide negative, positive
# for x in range(N):
#     if list_N[x] > 0 :
#         mid = x
#         break
# # print(f'mid = ', x)

# # 짝 지어주기
# # 아니 근데 0과 가까운걸 어떻게 정해주지..??
# min = max(list_N)   # what if max 값이 1이면? 
# min_left = 0
# min_right = 0
# for i in list_N[0: mid]:
#     for j in list_N[mid : N]:
#         if abs(i + j) < min:
#             min_left = i
#             min_right = j
#             min = abs(i + j)

# print(min_left, min_right)
# 3:11

# [Method 2] TWO POINTER 
'''
two pointer : '정렬된 리스트'에서 '두 개의 수를 골라' '조합 찾는거' 제격

1. 졍렬된 리스트 양끝에서 시작
2. 합이 음수면 left_ptr ++ 오른쪼긍로
3. 합이 양수면 right_ptr -- 왼쪽으로
4. 합이 0 이면 바로 종료
5. abs(합) 이 가장 작은 조합 저장
'''
# init idices
left = 0
right = N - 1

# assign values
min = float('inf')  # ? 오호 무작정 큰 수 대입하는 거
min_left = list_N[left]
min_right = list_N[right]

while left < right: # as long as not crossing each others # 이걸 몰라서 nested for loop 써버렸네
    sum = list_N[left] + list_N[right]

    if abs(sum) < min:
        # update vals needed
        min = abs(sum)
        min_left = list_N[left] # left, right 도 작은 애들값으로 업데이트
        min_right = list_N[right]

        if min == 0:
            # stop -> (case 4)
            break
    # othersie, if sum == negative, (case 2)
    if sum < 0:
        left += 1
    else:   # if sum == positive, (case 3)
        right -= 1

print(min_left, min_right)