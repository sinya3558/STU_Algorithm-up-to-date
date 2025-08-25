# https://www.acmicpc.net/problem/12919
"""
S,T 는 알파벳 A,B만 사용된 문장
1) 뒤에 A 추가
2) 뒤에 B 추가한뒤 문자열 뒤집
조건 두개만 써서 S -> T 가능한지 아닌지 알아내는 프로그램

# S와 T는 최대 최소 길이 차이가 min 1 정도 달라야함
# S 길이가 T보다 길면 안되,ㅁ 
"""
import sys

S = input()
T = input()

# check length of string
if not (1 <= len(S) <= 49) or not (2 <= len(T) <= 50):
    sys.exit()
if not len(S) < len(T):
    sys.exit()


# def is_match(string_s, string_t):
#     '''
#     function:
#         is_match : 문자열 string_s (S) 가 타겟 아웃풋인 string_t(T) 와 동일한지 아닌지 체크한다
#     arguments:
#         string_s(str) : T 가 될 수 있는지 확인할 문자열 S
#         string_t(str) : 타겟 문자열 T
#     retutn:
#         bool: 동일하면 True, 그렇지 않으면 False
#     '''
#     output = False
#     # # when lengh of string_s(S) gets to the same length of T (target string), exit the function
#     # if len(string_s) == len(string_t):
#     #     sys.exit()
#     
#     if string_s == T:
#         output = True
#     # if ends with 'B', add 'A' then flip the entire string
#     if string_s[-1] == 'B':
        
#     # if ends with 'A', append 'B'
#     elif string_s[-1] == 'A':   # 근데 문자열 'A','B'만 존재하는데 elif 대신 else 넣어도 되려나
        ### 아하 문제 잘못이해함. 명진님 말씀이 맞다
    
#     return output

def is_match(string_T, string_S):
    '''
    function:
        is_match : 문자열 string_T 가 S 와 동일한지 아닌지 체크한다
    arguments:
        string_T(str) : reverse tracking 으로 S 가 될 수 있는지 확인할 문자열 T
        string_S(str) : backward approach 로 타겟이 된 문자열 S
    retutn:
        bool: 동일하면 True, 그렇지 않으면 False
    '''
    output = False

    if string_T == string_S:
        output = True
        return output
    
    # when length of input string excceeds lengh of target string -> exit the func
    if len(string_S) > len(string_T):
        # sys.exit()
        return output
    
    updated_T = ''
    # backward = ''

    if string_T[-1] == 'A': # 이거 역순이라서 끝에 A 온 경우 이전에 그냥 A 더해준 경우 뿐, 두번째 조건은 성립 불가능
        updated_T = string_T[:-1]    # Update T(remove the last char of the stirng)
        output |= is_match(updated_T, string_S)

    if string_T[-1] == 'B': # 얘는 B 더해주고 뒤집었을 경우 뿐
        # Update T (flip the order then remove B which was the last char of the string)
        ### @@@ 아니 여기 왜 안되는거지 -> mutation code
            # backward = string_T[::-1]    # backward order
            # updated_T = backward[:-1]    # remove B
            # 아 혹시... 업데이트 하는 순서가 잘못된듯? -> 동사무소 갔다가 확인
        ### @@@
        updated_T = string_T[:-1][::-1]
        ### @@@ line 80 - 81 랑 line 83 뭐가 다른거지...같은 일 하는거 아닌가?
        output |= is_match(updated_T,string_S)

    return output


print(1 if is_match(T,S) else 0)
# result = is_match(T, S)
# print(result)
