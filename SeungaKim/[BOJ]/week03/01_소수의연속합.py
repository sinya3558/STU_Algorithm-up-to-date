# 7월 5주차 공통문제 
# https://www.acmicpc.net/problem/1644
'''
하나 이상의 **연속된** 소수의 합으로 표현되는 자연수들
[가능]
ex:     3 : 1가지 (=3)
        41 : 3가지 (= 2+3+5+7+11+13),(= 11+13+17), (=41)
        53 : 2가지 (=5+7+11+13+17), (=53)
[불가능]
ex:     20 : 0 (!= 7 + 13 -> 연속된 소수가 아님)

자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
'''
import sys
import pdb  # 디버깅용

N = int(input())
# check constraint
if not 1 <= N <= 4000000:
    sys.exit()

# 2부터 N 까지의 자연수 중 소수가 몇개인지 세어보고 싶음 -> 에라토스테네스의 체 (= 소수의 배수 소거법)
def get_primes(n):
    arr = [True for i in range(n+1)]            # 일단 N 까지의 모든 자연수 prime numbers 라고 가정
    # 소수 구할 때는 N ** (1/2) 까지만 N으로 나누어지는지 체크해 보면 됨, 나누어지는 자연수의 배수들은 어짜피 다 나눠지니까
    arr[0] = False
    arr[1] = False
    for i in range(2, int(N ** (1/2)) + 1) :    # 0과 1은 제외-> 소수 2부터 시작
        if arr[i] == True:  ### Q. 아니 왜 if N // i == 0 으로 하면 안되지?
            multiple = 2
            while i * multiple <= N:
                # pdb.set_trace() # python debugger
                """
                !! 이거 gdb 랑 비슷한듯
                n	다음 줄 실행 (next)
                s	함수 내부로 진입 (step in)
                c	중단 없이 계속 실행 (continue)
                q	디버거 종료 (quit)
                p 변수명	변수 값 출력 (예: p i, p arr)
                """
                arr[i * multiple] = False       # N으로 나누어지는 약수(divisors)들은 소거
                multiple += 1
    return arr

# # test: print out prime nums from arr
# for i in range(2, N + 1):
#     if get_primes(N)[i]:
#         print(i, end=' ')

# 연속된 소수의 합으로 나타낼 수 있는 경우의 수 구하기
# sliding window 써야할듯 = 연속된 데이터에 범위에서 만족하는 구간 찾기(list & two pointers)  
def count_possible_sum(arr, targret_N):
    prime_arr = [i for i in range(len(arr)) if arr[i]== True]   # range(len(arr))하...인덱스만 뽑아야지 바보야
    count = 0
    partial_sum = 0
    l_ptr = 0
    r_ptr = 0
    # count + 1 없을때까지 몇번이고 반복
    while True:
        if partial_sum >= targret_N:
            if partial_sum == targret_N:    # sum 값이 target N 과 동일할 경우만 거르기. 그 외는 arr 왼쪽(작은 수)으로 이동
                count += 1
            partial_sum -= prime_arr[l_ptr]
            l_ptr += 1
        elif r_ptr == len(prime_arr):
            #stop
            break
        else:
            partial_sum += prime_arr[r_ptr]
            r_ptr += 1
        # partial_sum = sum(prime_arr[l_ptr : r_ptr])
        # print("curr sum:", partial_sum, "| left:", l_ptr, "| right:", r_ptr)

    return count

# main
arr = get_primes(N)
print(count_possible_sum(arr, N))