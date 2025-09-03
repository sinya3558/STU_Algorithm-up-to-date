# 에라토스테네스의 체 : 특정 수의 범위안에 있는 수들 중 소수만 고르는 알고리즘
import math

N = 1000    # 2부터 1000(N)까지 모든 수에 대해서 소수만 골라ㅏㄹ
# 처음엔 모든 수가 소수(True) 인 것으로 초기화 (0과 1은 제외)
array = [True for i in range(N+1)]

# 에라토스테네스의 체
array[0] = False
array[1] = False

# for i in range(2, N + 1): 
for i in range(2, int(math.sqrt(N)) + 1):   # square root N 하는 이유는 약수가 saure root N 기준으로 symmetric
    # O(N) -> O(N^(1/2)) 엥? 이거 아님
    # O(N*loglogN) = nearly linear time
    # if its prime num,
    if array[i] == True:
        # i 를 제외한 i의 배수만 제거
        multiple = 2
        while i * multiple <= N:    # 범위 지정 까먹지 말 것
            array[i * multiple] = False
            multiple += 1

# print out all primes
for p in range(2, N + 1):
    if array[p]:
        print(p, end=' ')