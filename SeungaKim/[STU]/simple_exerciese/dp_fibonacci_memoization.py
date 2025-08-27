# dynamic programming : example of memoization usage
d_mem = [0] * 100

def fibo_mem(x):
	print('f(' + str(x) + ')', end=' ')
	if x == 1 or x == 2:
		return 1
	if d_mem[x] != 0:
		return d_mem[x]
	d_mem[x] = fibo_mem(x - 1) + fibo_mem(x - 2)
	return d_mem[x]

fibo_mem(10)