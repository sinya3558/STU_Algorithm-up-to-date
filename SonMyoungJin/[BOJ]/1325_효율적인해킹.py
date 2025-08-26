import sys
from collections import deque

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''

'''

N, M = map(int, input().split())
trust_rel = {i:[] for i in range(1, N+1)}

for _ in range(M):
    A, B = map(int, input().split())
    trust_rel[B].append(A)

def cnt_using_bfs(start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    cnt = 1 # 시작컴퓨터 포함
    
    while queue:
        cur = queue.popleft()
        for next in trust_rel[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                cnt += 1
    return cnt

max_cnt = 0
max_hack_computers = []

for com in range(1, N+1):
    hack_cnt = cnt_using_bfs(com)
    if hack_cnt >= max_cnt:
        max_cnt = hack_cnt
        max_hack_computers.append(com)

max_hack_computers.sort()        
#print(' '.join(map(str, max_hack_computers)))
print(*max_hack_computers)   
        
'''
# DFS 이용한 풀이
# 틀림...
max_cnt = -1
com_list = []

for _ in range(M):
    A, B = map(lambda x: int(x)-1, input().split())
    trust_rel[B].append(A)

for i in range(N):
    is_visited = [False] * N
    if len(trust_rel[i]) > 0:
        cnt = 1
        is_visited[i] = True
        stack = [i]
        while len(stack) > 0:
            cur_node = stack.pop()
            for next_node in trust_rel[cur_node]:
                if is_visited[next_node] == False:
                    cnt += 1
                    stack.append(next_node)
                    is_visited[next_node] = True

        if max_cnt < cnt:
            max_cnt = cnt
            com_list.append(i)
        elif max_cnt == cnt:
            com_list.append(i)
            
com_list.sort()
for com in com_list:
    print(com + 1, end = ' ')
    
print()
'''