#00:58:40.90
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
N개의 회의에서 각 회의시간(시작시각, 끝나는 시각)이 겹치지 않게 하는 최대 가능한 회의 갯수 구하는 문제
- 최대한 시간이 짧은 회의를 선택해야함.
- 시작시간이 0에 가까운순으로 선택해야함.
    => 이 경우가 부분적인 최선의 선택이고, 결과적으로 전체 최적의 해를 얻을 수 있기 때문에 => 그리디 알고리즘..
    => 빨리 끝나는 회의(끝나는 시각이 작은)는 시작시간이 0에 가까우면서, 시간이 짧음
    => 따라서, 끝나는 시각순으로 회의를 정렬 => O(NlogN)
1. 끝나는 시각순으로 회의 정렬 (그 다음은 시작시간순)
2. 이전 회의 끝나는 시각보다 시작시각이 크거나 같으면 회의 가능하므로 cnt올리고 회의 끝나는 시각 갱신. => O(N)

=> O(NlogN)
'''

N = int(input())
Meetings = []
for _ in range(N):
    Meetings.append(list(map(int, input().split())))

# 끝나는 시간순, 끝나는 시간같으면 시작시간순 (빨리 끝나는 회의부터 선택해야하니까)
Meetings.sort(key = lambda x: (x[-1], x[0]))
#print(Meetings)

cnt = 0
end_time = 0

for start, end in Meetings:
    # 시작 시각이 이전 회의 끝나는 시각보다 크거나 같으면 회의 가능
    if start >= end_time:
        cnt += 1
        end_time = end # 끝나는 시각 갱신
print(cnt)