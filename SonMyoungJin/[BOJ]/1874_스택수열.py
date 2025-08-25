#00:48.17.79
import sys

#sys.stdin = open("input.txt", 'r')

'''
1 ~ N까지의 수를 스택에 push하고 pop해 해당 수열을 만드는데 그 과정을 출력하는 문제
1. 목표 수열의 첫번째 숫자(4)까지 push
    - 무조건 오름차순으로 스택에 넣기 때문에 우선 4까지 push해야 pop해서 목표 수열 만들 수 있음
        - 현재 해당하는 숫자(스택에 넣을 숫자 1~N) 나타내기 위해 cur 변수 1로 초기화해서 선언
        - cur이 목표 수열(num_list)의 숫자(num) 4에 도달하기까지 stack에 push하고 +1
        - 4에 도달하면 stack에서 pop해준다
    - 현재 스택 맨위 숫자가 우리가 원하는 숫자와 다르면 수열 만들수 없어 plag = False
2. 목표 수열의 다음 숫자에도 그대로 적용 
'''

N = int(sys.stdin.readline().strip())
num_list = []
stack = []
cur = 1 # 스택에 넣을 숫자 (1 ~ N까지 오름차순으로 +1)
result = []
plag = True # 해당 수열 만들지 못할 경우를 적용하기 위해 선언

num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

for num in num_list:
    # 현재 숫자보다 작으면 계속 스택에 넣음
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1
    # 스택 맨 위 숫자가 우리가 원하는 숫자이면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    # 스택 맨 위 숫자가 우리가 원하는 숫자 아니면 불가능
    else:
        plag = False

print("\n".join(result) if plag else "NO")
    
