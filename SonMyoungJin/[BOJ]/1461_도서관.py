#01:05:16.25
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드 참고 : https://jaejae-sosp.tistory.com/79

모든 책을 제 위치에 둬야 할 때 최소 걸음 수를 구하는 문제
- 한번에 최대 M권들고 다시 책 가지러 0을 방문해야하는데 마지막 책은 0으로 돌아올 필요없음
- 먼 책부터 M개씩 묶어서 처리 -> 지금 할 수 있는 최선의 선택 => 그리디

1. 왼쪽(-) 방향, 오른쪽(+) 방향은 겹칠 일이 없으니까 따로 분리
    - 최소 이동을 위해서 각각 내림차순 정렬해서 가장 멀리 있는 것부터 M개씩 묶음
2. 묶음에서 가장 멀리있는게 이동거리니까 for문으로 0부터 len까지 M씩 건너뛰기
    - 0까지 다시 도착해 다음 정리할 책 들어야하니까 answer += 가장 멀리 있는 위치 * 2
    - 가장 큰 값은 한번만 가도록 나중에 뺄 수 있도록 max_dist에 max를 비교해 저장
'''

N, M = map(int, input().split())
book_numbers = list(map(int, input().split()))

neg = [] # 음수
pos = [] # 양수
for book in book_numbers:
    if book > 0:
        pos.append(book)
    else:
        neg.append(-book) # 절댓값으로 계산 편하게
        
neg.sort(reverse = True) # 큰 값을 앞으로 정렬
pos.sort(reverse = True)

answer = 0
max_dist = 0

# 음수 쪽
for i in range(0, len(neg), M):
    answer += neg[i] * 2
    max_dist = max(max_dist, neg[i])
    
# 양수 쪽
for i in range(0, len(pos), M):
    answer += pos[i] * 2
    max_dist = max(max_dist, pos[i])
    
# 가장 먼 곳은 돌아올 필요 없으니까 빼줌
answer -= max_dist
print(answer)