# https://www.acmicpc.net/problem/2562
'''
9개의 서로 다른 자연수 중 -> 최대값 찾고 그것의 순서를 구해라
ionput :
각 라인 하나씩 자연수 주어진다 (9번째 줄까지)
output :
첫째 줄에 최대값
둘째 줄에 순서 출력
'''
#10:12
import sys

# list comprehension && 난 왜 readline() 만쓰면 자꾸 런타임에러가 나.. 더 많이 써봐봐
user_inputs = list(int(sys.stdin.readline()) for _ in range(9))

# sorting
max_val = user_inputs[0]
place = 0
# enumerate() -> loop through iterable objects(list, tuple), then get value and index both
for idx , val in enumerate(user_inputs, 0):
    # constraint
    if val > 100:
        sys.exit()
    # update max val
    if val > max_val:
        max_val = val
        place = idx
    
print(max_val)
print(place + 1)    # place = index
# 10:41