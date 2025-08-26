#00:42:42.48
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
문자열 S를 문자열 T로 두가지 연산을 사용하여 바꿀 수 있는지 알아내는 문제
    - S 뒤에 'A'를 추가
    - S 뒤에 'B'를 추가하고 문자열을 뒤집기
- S를 T로 만드는 과정에서 연산에 따라 문자열을 만들면 너무 많은 경우의 수 발생,
    => 따라서, T에서 연산을 반대로 적용해 S를 만들 수 있는지 확인하는 게 더 효율적
    => T에서 시작해 S를 찾는 경우의 수는 가능한 연산이 2가지라서 여러 경로가 생길 수 있어서 DFS를 사용.

DFS는 재귀로 구현하니까
 1. 종료 조건
    - t == S => 변환 성공 True
    - len(t) < len(s) => t는 점점 짧아지는 연산중, 하지만 S보다 짧아지면 안되니까 False
 2. 변환 규칙
    - t[-1] == 'A' => t[:-1]가 다음 탐색 대상이고, 이게 변환 성공이면 바로 True
    - t[0] == 'B' => t[1:][::-1]가 다음 탐색 대상이고, 이게 변환 성공이면 바로 True
 3. 연산 모두 시도했는데 S에 도달못하면 실패니까 return False
'''

S = input()
T = input()

def dfs(t):
    if t == S:
        return True
    if len(t) < len(S):
        return False
    if t[-1] == 'A':
        if dfs(t[:-1]):
            return True
    if t[0] == 'B':
        if dfs(''.join(reversed(t[1:]))): ## t[1:][::-1] 앞의 B 떼고 문자열뒤집기
            return True
    return False

print(1 if dfs(T) else 0)

        
