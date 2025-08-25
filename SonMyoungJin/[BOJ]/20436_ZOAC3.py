#00:49:28.07
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
문자를 입력하기 위해 손가락을 이동하는 시간과 키 누르는 시간 1을 더해 해당 문자열 출력하는 데 걸리는 시간의 최솟값 구하는 문제
1. 이동하는 시간은 좌표로 계산되고, 키보드는 정해져있는 위치가 있으므로 keyboard배열로 키보드는 입력
    - 좌표 계산을 용이하게 하기 위해서 z를 0,0으로 하여 keyboard 배열 선언
2. 좌표 계산 함수 선언
    - char의 (x,y)좌표 얻기 위해, 배열에서 char해당하는 인덱스 얻기 위해 index 함수를 사용
3. 시작 손가락 위치와 현재 문자열의 좌표를 모두 구하고 오른쪽 범위를 지정해 이동시간 계산
'''

L, R = input().split()
input_str = input()

# Z => (0,0)
keyboard = [['z','x','c','v','b','n','m'],
            ['a','s','d','f','g','h','j','k','l'],
            ['q','w','e','r','t','y','u','i','o','p']]

def coord(char):
    for i in range(3):
        if char in keyboard[i]:
            j = keyboard[i].index(char) # arr에서 char있으면 그 인덱스 리턴하기위해서 index 함수 사용
            return (i, j)

start = [coord(L), coord(R)]
input_word = [coord(chr) for chr in input_str]
#print(input_word)

time = 0
for char_coord in input_word:
    if (char_coord[0] == 0 and char_coord[1] >= 4) or char_coord[1] >= 5: # 오른쪽으로 입력
        time += abs(start[1][0] - char_coord[0]) + abs(start[1][1] - char_coord[1]) + 1
        start[1] = char_coord
    else: # 왼쪽으로 입력
        time += abs(start[0][0] - char_coord[0]) + abs(start[0][1] - char_coord[1]) + 1
        start[0] = char_coord
print(time)