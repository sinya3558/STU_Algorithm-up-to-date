# simpe example of two pointers
N = 5   # 데이터 개수 (1, 2, 3, 2, 5)
M = 5   # 목표하는 부분 합의 값
data = [1, 2, 3, 2, 5]  # 데이터 전체 수열

count = 0
partial_sum = 0
end = 0

# start 차례대로 증가시키며 반복
for start in range(N): 
    # end 가능한 만큼 이동시키기
    while partial_sum < M and end < N:  # end 1씩 증가시키기 위한 end condition
        partial_sum += data[end]
        end += 1
    # 부분합이 M 이면 카운트 증가
    if partial_sum == M :
        count += 1
    partial_sum -= data[start]
print(count)