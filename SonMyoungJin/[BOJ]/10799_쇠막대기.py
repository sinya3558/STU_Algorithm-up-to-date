#00:32:38.23
import sys

#sys.stdin = open("input.txt",'r')

'''
쇠막대기의 시작과 끝을 효율적으로 추적하기 위해 LIFO방식으로 동작하는 stack을 사용.
1. '('를 만나면 쇠막대기 시작으로 보고 일단 스택에 넣음.
2. ')'를 만나면 :
    - 직전이 '('라면 레이져, 현재 스택에 있는 쇠막대기 모두 잘리므로 현재 스택 길이를 picecs에 더함.
    - 직전이 ')'라면 쇠막대기의 끝, 쇠막대기가 처음 레이저만날때 2조각으로 잘리므로 스택에서 '('꺼내고 picecs에 1 더함.
'''

arr= list(sys.stdin.readline().strip())

stack = []
picecs = 0

for i in range(len(arr)):
    if arr[i] == '(': # 쇠막대기 시작 이거나 레이져 시작
        stack.append(arr[i]) 
    else: #')' : 쇠막대기의 끝이거나 직전이 '('이면 레이져
        if arr[i-1] == '(':
            stack.pop()
            picecs += len(stack)
        else:
            stack.pop()
            picecs += 1 # 쇠막대기 끝이니까 1개 추가
            
print(picecs)
    