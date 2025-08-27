# bottom-up dynamic programming example

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 -> DP 가 dynamic programming 인가..
d = [0] * 100

# set up initial values
d[1] = 1
d[2] = 1
n = 10

# fibonacci sequence - bottom-up dynamic programming
for i in range(3, n + 1):
	d[i] = d[i-1] + d[i-2]
	
print(d[n])