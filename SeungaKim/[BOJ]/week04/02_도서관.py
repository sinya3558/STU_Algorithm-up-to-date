# https://www.acmicpc.net/problem/1461
# 그리디 알고리즘 (설명 15:09)
# 16:28
# 17:21 (53분 + 49분)

# 1. 문제 설명
'''
- 세준이의 현재 위치 0
- 돌려놓아야 할 책들의 위치 또한 0
- 한번에 들 수 있는 책 M 권
- 한 걸음에 좌표 1칸씩 이동
- 모든 책을 제자리에 놔둘 때 드는 **최소 걸음 수**를 계산하기 ( 책의 위치는 정수 좌표)
- 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요 없음
'''
# 2. 문제 해결 아이디어
'''
- 최소 걸음 수 계산 : sorting
- x 축으로만 이동하니까 2d 는 필요 없고
- 왔다 갔다 이동하는 것만 좀 고려하면 되지않을까
'''
# 3. 분석
'''
- 왜 자꾸 틀리는지 GPT 참조함 : 
- 음수랑 양수 분리 안하면 양쪽을 동시에 다녀오는(?) 계산 발생 -> 그래서 자꾸 예상아웃풋이랑 다르게 나오는듯?
- 핵심 : 책을 놓으러 갈 때는 한쪽(negtive, positive) 만 다녀와야 한다
- 한쪽씩 (neg, pos) 나누어서 가장 먼 값부터 M 개씩 묶어 처리 -> 그리디하게 최적
- 마지막만 furthest 편도로 한번 처리(이 거리만큼 빼준다)
'''
# 4. 코드
import sys

# 사용자 인풋 입력 받기
N, M = map(int, input().split())
# print(f'N : ', N)
# print(f'M : ', M)
if not 0 <= N <= 50 or not 0 <= M <= 50:
    sys.exit()

list_books = list(map(int, input().split()))
# print(list_books)
for i in list_books:
    if abs(i) > 10000:
        sys.exit()


def print_short_path(n, m, position) :
    '''
    input parameters
        n = 책의 개수 N
        m = 한번에 드는 책의 수 M
        position = 책의 위치가 입력된 리스트

    rt_val
        steps = 움직인 최소 거리(int)
    '''
    steps = 0           # 최소 걸음 수
    
    # 원점 기준으로 negative, positive position 나누기
    p_position = sorted([x for x in position if x > 0], reverse=True)   # discending order
    n_position = sorted([-x for x in position if x < 0], reverse=True)  # 절대값 큰 negative 순으로 -> 여기는 음수라 ascending(=절대값 discending)

    # 최대 거리 책 위치 찾기
    furthest = 0        # 포지션 리스트 안에 가장 멀리 있는 책 위치 값
    # pos, neg 나눠놨으니 둘 중에 큰 값 각자 고르고 다시 걔네끼리 비교 확인
    if p_position:
        furthest = max(furthest, p_position[0])     # update furthest
    if n_position:
        furthest = max(furthest, n_position[0], key=abs)     # neg 쪽 최대값이랑 비교

    # 책 M 개씩 묶기
    ## positive 
    for i in range(0, len(p_position), m):
        steps += p_position[i] * 2
    ## negative
    for i in range(0, len(n_position), m):
        steps += n_position[i] * 2

    steps -= furthest   # 마지막 책은 원점 안돌아가니까 왕복 횟수 차감

    return steps

    '''
    book_left = n       # 남아있는 책의 권 수
    furthest = 0        # 리스트안에 있는 가장 멀리 있는 북 포지션 값
    list_books = []     # 북 포지션 값들 M 개씩 나눠 저장해둔 리스트

    # sort the list in ascending order first
    sorted_books = sorted(position)

    # 최대 거리 위치 제외한 나머지들 -> M 개씩 묶기
    furthest = max(sorted_books, key=abs)    # 참조, 그냥 max() 로 빼내니까 negtive 경우에 리스트에서 그 값이 제외되지 않았음 -> 아? 뭐지 다시보니까 당연한 소리 적어뒀네
    # print(furthest)
    # 만약 furthest 가 음수값이면, 리스트 sort discending order, 양수값이면 그대로 진행
    if furthest < 0 :
        sorted_books = sorted(sorted_books, reverse=True)

    # 책 M 개씩 묶기
    for x in range(0, len(sorted_books), m) :
        # print(sorted_books[x : x + m])    # 참조, 슬라이싱 까먹어서 코드 진행이 안됨;
        list_books.append(sorted_books[x : x+m])    # 잉 근데 이러면 리스트 안에 리스트..? nested list
    # nested list 접근해보쟈
    for group in list_books:    # M 개씩 그룹 나눈 list_books 에서 그룹들 확인
        # for ele in group:       # 각 그룹 list 사이에 elements 확인
        #     max_val = max(ele)
        max_val = max(group, key=abs)
        # 근데 마지막 책일 경우(=furthest)
        if max_val == furthest:
            steps += abs(furthest)
        else:
            steps += abs(max_val) * 2
    return steps
    '''
# print out output
print(print_short_path(N, M, list_books))


