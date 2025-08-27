# dynamic programming 
'''
n x m 금광이 1x1 로 나뉘어져 있을 때, 
첫 번째 열 **아무 행**에서 부터 출발, m - 1 번에 걸쳐 매번 오른쪽 위/오른쪽/오른쪽 아래 3 가지 방향중 하나의 위치로 이동해야함
채굴자가 얻을 수 있는 금의 최대 크기를 출력하라

1 3 3 2
2 1 4 1
0 6 4 7

얻을 수 있는 금의 최대 크기 : 19
'''
# 오.. 대각선 이동...? 근데 8 개중에서 3개만 따로 어떻게 하지
'''
인풋 조건:
- 첫째 줄에 테스트 케이스 T (1 <= T <= 1000)
- 매 테스트 케이스 첫째 줄에 n & m (1<=n, m <=20)
- 둘째 줄에 n x m 위치에 할당 된 금의 개수 (1 <= 금 개수 <= 100)

아웃풋 조건:
- 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 추렭
각 테스트 케이스는 줄바꿈으로 구분한다 (\n)
'''
'''
ex.
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

19
16
'''
# gold[r][c] = 파뭍혀 있는 금의 양
# dp[r][c] = 최적의 해 ( 얻을 수 있는 최대 금의 크기)
## 오른쪽 위/오른쪽/오른쪽 아래
### dp[r][c] = gold[r][c] + max(dp[r-1][c+1], dp[r][c+1], dp[r+1][c+1])

# # 일단 dp table 초기화
# dp[r][c] = 101 # max 금 개수 100개

# # 범위 체크 -> 막히는 곳 있나 없나

# 테스트 케이스 받기
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    gold_list = list(map(int, input().split()))

    # dp table
    dp = []
    idx = 0
    # 1d 로 받은 금광 값들 n x m 행렬에 채워주기
    for r in range(n):
        # 어느 행이나 가능... 이걸 어떻게 하죠
        dp.append(gold_list[idx : idx + m])
        idx += m
    
    # 다이나믹 프로그래밍 - bottom-up 
    for c in range(1, m) : # 시작 행 제외한 나머지 
        for r in range(n):  # 
            # ? 엥 오는 방향을 확인해주네
            # **왼쪽 위/왼쪽/왼쪽 아래에서 오는 경우들**
            # dp[r][c] = gold[r][c] + max(dp[r-1][c-1], dp[r][c-1], dp[r+1][c-1])
            
            # 왼쪽 위에서 오는 경우
            if r == 0:  # 두번째 행, 첫 번째 열
                left_up = 0 # 더 이상 위로 갈 공간 없슴
            else:
                left_up = dp[r - 1][c - 1]
            
            # 왼쪽 아래에서 오는 경우
            if r == n - 1:
                left_down = 0
            else:
                left_down = dp[r + 1][c - 1]
            
            # 왼쪽에서 오는 경우,
            left = dp[r][c - 1]
            dp[r][c] = dp[r][c] + max(left_up, left_down, left)
    
    # 최고 금의 크기 계산
    cnt = 0
    for x in range(n):
        cnt = max(cnt, dp[x][m - 1])     # 그니까 각 열 마지막 행까지 다
    print(cnt)        

# 학교 과제 데쟈뷰 같다
