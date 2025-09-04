# https://school.programmers.co.kr/learn/courses/30/lessons/389480
# 13:45
'''
n : A의 흔적 누적 개수 맥시멈, n개 이상 -> 붙잡힘
m : B의 흔적 누적 개수 맥시멈
info : 2d list of 흔적 = [A, B]
'''
import sys
import ast      # ast: abstract syntax tree
# get user inputs 
# cnt_info = int(sys.stdin.readline()) 
# info = []
# for _ in range(len(cnt_info)):
#     theif_a, theif_b = map(int, sys.stdin.readline().split())
#     info.append(theif_a, theif_b)
# info 처리하는게 어렵구만

# info 리스트로 받는거 참조함
user_input = sys.stdin.readline().strip()   # strip() -> del '\n'
str_info, str_n, str_m = user_input.rsplit(maxsplit=2)  # "rsplit" -> reverse split & "maxsplit = n" -> 뒤에서 n 번째까지만 split
# print(str_info, str_n, str_m)
# 14:28

# 14:38
# convert str to list and ints
# str -> list 참고함
list_info = ast.literal_eval(str_info)  # convert string [[]] itself to actual list [] in python
# so you can iterate lsit_info as a list
if not 1 <= len(list_info) <= 40:
    sys.exit()
# str -> int
n = int(str_n)
m = int(str_m)

def solution(info, n, m):
    answer = 0  # min(A의 누적 흔적) -> answer : 안걸리고 넘어갈 수 있는 A의 최소 범행 수
    for i in range(len(info)):
        # 최적의 확률 어떻게 구한담? + dp table 동작 과정 이해 필요
        # a = info[i][0]
        b = info[i][1]
        temp_b = 0
        temp_a = 0
        # while temp_b < m:

    return answer

print(solution(list_info, n, m))