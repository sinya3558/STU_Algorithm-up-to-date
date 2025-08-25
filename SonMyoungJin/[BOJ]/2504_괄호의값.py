#01:21:07.09
import sys

#sys.stdin = open("input.txt",'r')
'''
코드 참고: https://hongcoding.tistory.com/114

(()[[]])([]) 
=> 2*(2+3*3)+2*3
=> 2*2 + 2*3*3 + 2*3 곱하기 먼저하고 더하기 한다고 생각

1. 괄호열이 올바른지 체크 필요
    - 스택으로 짝이루는지 확인하면 됨
2. 괄호열의 값을 계산 (괄호의 깊이 추적하며 계산)
    - 열린 괄호 등장할 때마다 값을 설정
    - 계산값을 추적하기 위해 tmp 변수 사용 
    - 닫힌 괄호 등장할 때 "값을 계산"
    - result 변수를 사용해 추적한 tmp 값을 더함
        ex)
            ')'일 떄,
            직전이 '(' 이면, tmp * 2 하고 값을 result에 합산, '('를 pop
                        그리고 합산 했으니까 tmp //= 2 해줌
            직전이 '[' 이면, 옳바르지 않은 괄호열
            직전이 ']' 이면, 이미 곱한 값을 합산한 후 이므로 ']'를 pop, tmp //= 2
'''
p_str = sys.stdin.readline().strip() #뒤에 공백을 제거하자! 제거 안하면 틀림

stack = []
result = 0
tmp = 1

for i in range(len(p_str)):
    # 열린 괄호 만나면 push하고, 임시 tmp 값에 각 값을 곱해줌
    if p_str[i] == '(':
        stack.append(p_str[i])
        tmp *= 2 # 깊이 증가

    elif p_str[i] == '[':
        stack.append(p_str[i])
        tmp *= 3
    #닫힌 괄호 ')' 일 때
    elif p_str [i] == ')':
        # 스택이 비었거나 대칭 안맞으면 올바르지 않은 괄호열
        if not stack or stack[-1] == '[':
            result = 0
            break
        # 직전이 '(' 면 안에 괄호 안에 아무 값도 없다는 뜻이니까 tmp값을 result에 합산
        if p_str[i-1] == '(':
            result += tmp
        # 열린 괄호 '(' pop
        stack.pop()
        # 괄호 하나 닫았으니까 깊이는 반으로 줄임
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if p_str[i-1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3
# 스택에 남은 괄호 있으면 잘못된 괄호열이므로 0 출력
print(result if not stack else 0)