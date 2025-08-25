# second attempt of 도서관
# https://www.acmicpc.net/problem/1461
# 이것도 투포인터로 나누면 안되나?
'''
문제
- 현재 위치 0, 책 제자리에 돌려놓기
- 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하여라 (한 걸음에 좌표 1칸)
- 책을 모두 제자리에 놔둔 후에 다시 0으로 돌아올 필요 없다

input
- 첫째 줄 N(책의 개수), M(한번에 들 수 있는 책의 개수), 0 <= N, M <= 50
- 둘째 줄 list(책의 위치. space랑 함께), 0 < abs(book_position) < 10000

output
- steps (총 걸음 수)
'''
# 4:38
import sys
# user input
N, M = map(int, input().split())
if not 0 < N <= 50 or not 0 < M <= 50:
    sys.exit()
book_position = list(map(int, input().split()))
for x in range(len(book_position)):
    if not 0 < abs(book_position[x]) <= 10000:
        sys.exit()
# print(N, M, book_position)

# sort position of books based on negative & positive
book_position.sort()    # ascending order
# print(book_position)
neg_books  = []
pos_books = []
# divide them into two
for x in range(len(book_position)):
    if book_position[x] > 0 :
        pos_books.append(book_position[x])
        # 아....찾았으면 멈춰야지
    else:   # otherwise,
        neg_books.append(-book_position[x]) # last index of the array

# update positions
neg_books = sorted(neg_books, reverse=True)  # discending, neg[0] -> abs min distance / neg[div] -> max distance
# print(f'sorted ng_books = ', neg_books)
pos_books = sorted(pos_books, reverse=True)
# print(neg_books, pos_books)

# find the furthest book position
max_dist = 0
# if negative vals exist,
if neg_books :
    max_dist = max(max(neg_books, key=abs), max_dist)
# else:
#     max_dist = 0
if pos_books :
    max_dist = max(max(pos_books), max_dist)    # compare max


min_steps = 0
# grouping position by M -> Q. 어떻게 하더라?
# M 개씩 그룹 묶어주기
# for i in range(len(neg_books) - 1, -1, -M):
for i in range(0, len(neg_books), M):
    min_steps += abs(neg_books[i]) * 2 
for i in range(0, len(pos_books), M): # reverse needed?
    min_steps += pos_books[i] * 2
min_steps -= max_dist
# print(f'max =', max_dist)

print(min_steps)
# 7:02
# 엥, 왜 답이 다르니?