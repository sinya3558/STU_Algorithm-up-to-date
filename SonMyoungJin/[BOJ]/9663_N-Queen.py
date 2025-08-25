#02:00:00.00
import sys

#sys.stdin = open("input.txt", 'r')

'''
코드 참고: https://velog.io/@kjy2134/%EB%B0%B1%EC%A4%80-9663-N-Queen-%ED%8C%8C%EC%9D%B4%EC%8D%AC

체스에서 퀸은 상하좌우 대각선 모두 끝까지 이동 가능.
퀸이 서로를 잡지 못하게 놓으려면 퀸이 하나 놓인 자리에 같은 행, 같은 열, 대각선은 놓으면 안됨.
- 내가 퀸 놓은 위치 기준으로 다음 퀸을 놓을 자리 탐색하므로 DFS
- 퀸을 못 놓는 자리이면 이전으로 돌아가 다른 경우를 탐색해야하므로 백트래킹

1. N*N 체스판에 N개의 퀸을 모두 두려면 각 행마다 퀸 하나씩만 둘 수 있음
    - 따라서, 행마다 하나씩 두니까 열, 대각선 2방향만 제외 표시
    - 퀸이 놓일 수 없는 배열 관리 위해 exc_col, exc_up, exc_down 배열 선언
2. 현재 행에서 i번째 열에 퀸을 놓을 수 있는지 확인 필요
    - exc_col[i], exc_up[i], exc_down[i]가 False이면 제외되지 않았다면 놓을 수 있음
    - 퀸을 놓을 수 있으면, 해당 위치의 대각선 두방향 제외해야 하므로 모두 True로 바꿈
3. 다음 행으로 퀸을 놓기 위해 DFS 재귀호출
4. 퀸 놓고 다음 행으로 이동했는데, 해당 위치가 더 이상 유효하지 않으면 되돌려서 다른 경로 탐색하도록
    - 특정 행에 퀸 놓고, 그 후에 다른 행에서 놓을 수 있는 자리 없으면
    - 모든 퀸 놓았을 때
    - exc_col[i], exc_up[i], exc_down[i]가 False로 바꿈

* 대각선 번호
y = x (N-1, N-1)
(a,b),(a-i,b+i)
a+b = (a-i) + (b+i) (행 번호 + 열 번호)
N=4일때,
(0,0)       => 대각선 번호 0
(0,1),(1,0) => 대각선 번호 1 (n_q+1) (0+1) (1+0)
(1,1)       => 대각선 번호 2 (n_q+1)
(2,2)       => 대각선 번호 4 (n_q+2)
(3,3)       => 대각선 번호 6 (n_q+3)

y = -x (0, N-1) (1,N-2),,, (N-1,0)
(a,b), (a+i,b+i)
a-b = (a+i) - (b+i) (행 번호 - 열 번호) + (N - 1) 0부터 접근하려고 +(N-1)
N=4일때,
(0,3)       => 대각선 번호 -3 + 3 == 0 (n_q - i) + (N - 1)
(0,2),(1,3) => 대각선 번호 -2 + 3 == 1
(1,2)       => 대각선 번호 -1 + 3 == 2  
(2,1)       => 대각선 번호  1 + 3 == 3 
(3,3)       => 대각선 번호  3 + 3 == 6
번호 0 ~ 2*N-2까지 존재 
'''
# n_q : 놓은 퀸 개수이자 놓은 행의 번호
def DFS(n_q, N, exc_col, exc_up, exc_down):
    global cnt
    if n_q == N: # 모든 퀸 놓았으므로 경우의 수 증가
         cnt += 1
         return
    
    # 현재 행(n_q)에서 가능한 열 찾음
    for i in range(N):
        # 열, 대각선 2방향 확인했을 때 모두 false이면
        if not exc_col[i] and not exc_up[n_q+i] and not exc_down[n_q-i+(N-1)]:
            # 퀸 놓을 수 있으니까 해당 위치를 True로 설정해 퀸 다음에 놓을 때 제외시킴
            exc_col[i] = True 
            exc_up[n_q+i] = True
            exc_down[n_q-i+(N-1)] = True
            
            # 다음 행으로 퀸 놓기 위해 재귀 호출
            DFS(n_q+1, N, exc_col, exc_up, exc_down)
            
            # 퀸을 놓았던 상태를 되돌림(백트래킹)
            exc_col[i] = False
            exc_up[n_q+i] = False
            exc_down[n_q-i+(N-1)] = False

def N_queen(N):
    global cnt
    cnt = 0 # 경우의 수 세는 변수
    exc_col = [False] * N # 제외 열
    exc_up = [False] * (2 * N - 1) # 제외 대각선 y=x 
    exc_down = [False] * (2 * N - 1) # 제외 대각선 y=-x
    
    DFS(0, N, exc_col, exc_up, exc_down)
    return cnt

N = int(sys.stdin.readline().strip())           
print(N_queen(N))


'''
chess = [[-1] * N for _ in range(N)] # -1: 아무것도 안함, 0: 아무것도 놓지 못함, 1:queen 존재
queen = []
def DFS(row, col, chess, queen):
    if 0 <= row < N and 0 <= col < N:
        if (row, col) not in queen and chess[row][col] == -1:
            queen.append((row, col))
            chess[row][col] == 1
            for i in range(row+1, N):
                chess[i][col] = 0
                chess[row][i] = 0
                chess[i][i] = 0
            
            #DFS(row - 1, col, chess, queen)
            #DFS(row + 1, col, chess, queen)
            #DFS(row, col - 1, chess, queen)
            #DFS(row, col + 1, chess, queen)
'''