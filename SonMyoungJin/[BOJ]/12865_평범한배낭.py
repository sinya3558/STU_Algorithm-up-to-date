#01:04.14.58
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드 참고 : https://www.acmicpc.net/board/view/148327

주어진 무게 제한(K) 내에서 물건들(N개)을 배낭에 담을 때, 물건들의 조합이 가장 최대의 가치일때를 찾아내는 문제
- 각 물건을 선택하거나 선택하지 않으면서 가치를 계산하는 방식에서 동일한 상태는 여러 번 계산하지 않도록 
값을 계속 재사용해야하니까 DP 사용.

1. 우선순위 : 가치 > 무게 (무게 6, 무게 7 중 가치가 높은 게 6이라면 그 가치합이 정답)
    => 배낭 무게(용량)마다의 가치를 고려해주어야 함, 그리고 K까지로 제한 해야함.
    => 따라서, dp 배열은 i번째까지 물건까지 고려했을 때, 배낭무게를 0~K일 때의 각각의 가치를 고려해주도록
    => dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

2. 모든 물건을 하나씩 고려
    - 현재 물건 아직 안넣었을 때 최대가치는 dp[i+1][j] = dp[i][j].
    - 배낭의 무게(0~K)가 현재 물건 무게보다 작으면 못넣으니까 넘어감.
    - 현재 물건 넣을 수 있으면 현재 물건의 용량(w)만큼 비워져 있던 가치값에 현재 가치값 v 더함
    - 이전 값과 물건넣은값 중 가치값이 더 큰게 dp[i+1][j]로 저장.
    - 따라서, 최대 용량에서의 최댓값은 dp[N] 
    

시간복잡도: O(N*K)
'''

N, K = map(int, input().split())
Things = []
for _ in range(N):
    Things.append(list(map(int, input().split())))

# i번째 물건까지 고려했을 때, 배낭의 무게가 j일 때, 가질 수 있는 최대의 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# 모든 물건을 하나씩 고려
for i in range(N):
    w, v = Things[i]
    for j in range(K+1): # 배낭의 용량이 K까지 이기 떄문에
        dp[i + 1][j] = dp[i][j] # 현재의 물건 아직 안넣었을 때 최대 가치
        if j < w: # 배낭의 무게가 현재 물건 무게보다 작으면 못 넣으니까 넘어감
            continue
        # 현재 물건 넣을 수 있으면, 배낭 용량을 j-w만큼 비우고 
        # 비웠을 때의 최대 가치(dp[i][j-w])에 현재 가치 v 더함
        # 둘 중 가치합 더 큰 게 답
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
        
print(max(dp[N]))
#print(dp)