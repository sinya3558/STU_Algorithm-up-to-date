# 에라토스테네스의 체
## 1. 여러 개의 수가 소수인지 아닌지 체크할 때
## 2. 특정 수(N) 보다 작거나 같은 모든 소수를 찾을 때
import math
import pdb

# 단일 숫자 체크할 때
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):   # 0과 1은 고려x
        if n % i == 0:
            return False
    return True

# 여러 숫자 체크할 때
def are_primes(n):
    arr = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:   # 여기 빼먹음. 빼먹으니까 그냥 수의 나열임. 바보
                # print(f"TEST line: {i*j} as False (i={i}, j={j})") # 디버깅용 테스트
                # pdb.set_trace() # python debugger
                """
                !! 이거 gdb 랑 비슷한듯
                n	다음 줄 실행 (next)
                s	함수 내부로 진입 (step in)
                c	중단 없이 계속 실행 (continue)
                q	디버거 종료 (quit)
                p 변수명	변수 값 출력 (예: p i, p arr)
                """
                arr[i*j] = False
                j += 1
    return arr    


if __name__ == "__main__":
    # n = 4
    # print(is_prime(n))
    # n = 17
    # print(is_prime(n))
    n = 8
    for i in range(2, n + 1):
        if are_primes(n)[i]:
            print(i, end=' ')