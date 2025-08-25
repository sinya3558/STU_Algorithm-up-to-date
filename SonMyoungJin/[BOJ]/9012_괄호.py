import sys

#sys.stdin = open("input.txt", 'r')

'''
올바른 괄호 문자열(Valid PS, VPS)인지 확인하는 알고리즘:
- "("를 만나면 스택에 push
- ")"를 만나면 스택에 pop
- 스택이 비어있다면 VPS, "YES" 출력
- 스택에 요소 남아있어 짝이 맞지 않으면 VPS 아니므로 "NO"
'''

# 테스트 케이스 수부터 받아서 변수 N에 저장
# sys.stdin.readline() 하면 끝에 \n붙음 삭제하려면 .strip()
N = int(sys.stdin.readline())

# 각 테스트 케이스 처리를 위한 for문
for i in range(N):
    p_str_line = sys.stdin.readline().strip() # 테스트 케이스 p_str_line에 저장
    stack = [] # 괄호 저장할 스택 선언
    is_VPS = True # VPS 여부 확인 변수
    
    # 문자열의 각 문자를 하나씩 처리
    for c in p_str_line:
        
        # '(' 나오면 스택에 추가
        if c == '(':
            stack.append(c)
            
        # ')' 나왔을 때 스택에 '(' 있으면 pop
        elif c == ')':
            if stack:
                stack.pop()
            
            # 스택에 짝 맞출 "(" 없으면 VPS 아님
            else:
                is_VPS = False
                break
            
    # 처리 후 "(" 남아 있으면 VPS 아님
    if stack:
        is_VPS = False
    
    print("YES" if is_VPS else "NO")