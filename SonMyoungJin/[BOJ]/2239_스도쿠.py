#02:32:40.22
import sys

sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드 참고: GPT
스도쿠 퍼즐: 9*9보드에서 빈칸을 알맞은 숫자로 채우는 문제
    - 빈칸을 채우는 모든 경우의 수를 탐색하면서 규칙에 맞는지 검사하고 맞지 않으면 되돌려야하므로 백트래킹 뮨재
1. 빈칸 좌표를 따로 저장하기 위해 empties 배열을 선언해 저장
2. 행, 열, 박스에 어떤 숫자가 있는지 미리 체크하기 위해 set으로 집합배열 만듦
    - 각 행, 열, 박스에 0이 아닌수를 미리 저장해놓기 위해 rows, cols, boxes에 for로 접근하여 add
    - 박스는 3*3이므로 (i//3)*3 + (j//3)번째 박스
        - (4,7) -> (4//3)* 3 + (7//3) => 6번쨰 박스
3. 백트래킹
    - 빈칸접근인덱스 idx를 받아서 시작
    - 모든 빈칸을 다 채웠으면 출력하기 위해 len(empties) == idx이면 출력하고 시스템 종료
    - 빈칸에서 좌표꺼내기 위해 r,c = empties[idx]하고 box_idx도 계산
    - 사전식으로 작은 수부터 배치하기 때문에 for문으로 1 ~9 까지 시도
    - 시도한 숫자 num이 rows, cols, boxes에 없으면 숫자를 놓기 => board[r][c] = num, 그리고 num을 add
    - 놓고 나면 다음 칸을 탐색해야하므로 dfs(idx+1)를 재귀적으로 호출
    - 규칙안맞으면 백트래킹하기 위해 board[r][c] == 0, num은 remove
'''

board = []
for _ in range(9):
    # 문자열을 리스트로 바꾸면 문자단위로 쪼개짐 split()은 공백기준
    board.append(list(map(int, input()))) 

# 빈칸 좌표 저장
empties = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empties.append((i, j))

# 행, 열, 박스 어떤 숫자있는지 미리 체크
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            rows[i].add(num)
            cols[j].add(num)
            box_idx = (i//3) * 3 + (j//3)
            boxes[box_idx].add(num)

#print(rows)
#print(cols)
#print(boxes)
 
def dfs(idx):
    # idx : 빈칸 리스트 접근 인덱스
    # 다 채웠으면 답 출력
    if idx == len(empties):
        for row in board:
            print(''.join(map(str,row)))
        sys.exit(0) # 답 찾으면 즉시 종료
        

    # 빈칸 좌표 꺼내기      
    r, c = empties[idx]
    box_idx = (r//3) * 3 + (c//3)

    #print(idx, r, c)
    
    # 1 ~ 9까지 시도
    for num in range(1, 10):
        if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                # 숫자 놓기
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)

                dfs(idx + 1) # 다음 칸 탐색

                # 백트래킹
                board[r][c] = 0
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_idx].remove(num)

dfs(0)

''' 이거 쓰면 시간초과
# 행, 열, 박스 체크 함수
def is_valid(r, c, num):
    # 같은 행에 num 있는지
    for j in range(9):
        if board[r][j] == num:
            return False
        
    # 같은 열에 num 있는지
    for i in range(9):
        if board[i][c] == num:
            return False
        
    # 같은 박스에 num 있는지
    br, bc = (r//3) * 3, (c//3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == num:
                return False
            
    # 다 확인 했는데 괜찮으면 True
    return True
'''