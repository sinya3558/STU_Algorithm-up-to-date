#00:33:19.21
import sys

#sys.stdin = open('input.txt', 'r')

'''
1부터 N까지의 수 중에서 중복 없이 M개의 수를 고르는 문제
- 가능한 모든 수를 고르는 과정에서 중복을 방지하고, 한번 고른 거는 안고르도록 해야함.
- 가능한 수를 차례대로 고르고, 고른 수 M개 되면 그 수열 출력 해야함
    => 따라서, 백트래킹을 활용해 순열 구함.
'''
N, M = map(int, sys.stdin.readline().split())
visited = [] # 이미 고른 숫자를 표시하기 위한 리스트
seq = [] # 수열저장을 위한 리스트

def backtrack(N, M, seq, visited):
    # M개 숫자 뽑은 수열 완성했을 때
    if len(seq) == M:
        # seq는 숫자로 이루어진 리스트 이므로
        # 숫자 사이에 공백 넣기위해 join 사용
        # join은 iterable한 str 필요하므로 map으로 seq 요소 str 변환
        print(" ".join(map(str, seq)))
        return
    # 1부터 N까지 숫자 하나씩
    for i in range(1, N+1):
        # 방문하지 않은 숫자만 선택
        if i not in visited:
            visited.append(i) # 선택된 숫자는 방문 처리
            seq.append(i) # 수열에 숫자 추가
            backtrack(N, M, seq, visited)
            seq.pop() 
            visited.pop()

backtrack(N, M, seq, visited)

'''
import itertools

#sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

# 1부터 N까지의 숫자 중에서 M개를 고른 순열 생성
sequences = itertools.permutations(range(1, N + 1), M)

# 각 순열을 출력
for seq in sequences:
    print(" ".join(map(str, seq)))
'''