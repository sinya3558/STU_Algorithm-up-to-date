# top-down dynamic programming example

# 한 번 계산된 결과를 메모이제이션 (Memoization) 하기 위한 리스트 초기화
d = [0] * 100

# Fibonacci sequence 를 재귀함수로 구현 (top-down dynamic programming)
def fibo(n):
	# 종료 조건(1 or 2 이면 1을 반환)
	if n == 1 or n == 2:
		return 1
	# 이미 계산한 적 있는 문제라면 그대로 반환 -> memoization
	if d[n] != 0:
		# print(f'memorized:', d[n])
		return d[n]
	# 계산한 적 없는 문제라면, 피보나치 결과 내보냄
	d[n] = fibo(n-1) + fibo(n-2)
	return d[n]
	
print(fibo(10))