# 구간 합 상수 시간으로 빠르게 계산하기 : prefix sum 이용
# P 테이블 이용

N = 5   # 데이터 개수
data = [10, 20, 30, 40, 50]

# Prefix sum cal
sum_val = 0
prefix_sum = [0]
for i in data:
    sum_val += i    # data 값들의 부분 합 저장
    # prefix_sum[i] = sum_val 가 아니지..테이블에 넣어줘야지
    prefix_sum.append(sum_val)

# 구간 합 계산 예시 : 세 번째 수부터 다섯 번째 수까지의 부분 합은?
left = 3
right = 5
print(prefix_sum[right] - prefix_sum[left - 1]) # left-1은 ㅇ니덱스 1부터 쓰기위해