#01:30:08.96
import sys

#sys.stdin = open('input.txt','r')
'''
코드 참고: https://velog.io/@galong/%EA%B8%B0%ED%83%80-%EB%A0%88%EC%8A%A8-%EB%B0%B1%EC%A4%80-2343%EB%B2%88-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

주어진 M개의 블루레이에 강의를 나눠 담는 최소 블루레이 크기 찾는 문제
- 주어진 범위 내에서 최소값 찾기 => binary search 사용하면 효율적?
- 블루레이 크기를 찾는 문제니까 블루레이 크기의 범위가 주어진 범위
    - 그 블루레이의 크기는 강의 길이의 합 => 강의 길이의 합이 탐색 대상이 되는 것
최소 블루레이 크기(left) == 가장 큰 강의 길이
최대 블루레이 크기(right) == 모든 강의 길이의 합

1. binary search를 위해 최소, 최대 블루레이 크기의 중간값 mid를 정의
2. mid값에 대해 강의를 하나씩 더해가며, 현재 블루레이에 담을 수 있으면 담고, 아니면 블루레이 하나 추가
    - 강의들의 합이 mid보다 크면 블루레이를 하나 더 써야함
        - cnt올리고, 현재 강의부터 블루레이에 넣도록 현재 합을 현재 강의 길이로 초기화.
    - 강의들의 합이 mid보다 작거나 같으면 현재 합에 현재 강의 길이 더함.
3. M개이하의 블루레이로 처리할 수 있는지 체크
    - M개 넘으면 더 큰 강의 길이 합을 적용하므로 left = mid + 1
    - M개 안 넘으면 더 작은 강의 길이 합을 적용할 수 있는지 확인 right = mid - 1
'''

N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

def binary_search(N, M, lectures):
    left = max(lectures) # 최소 블루레이 크기는 가장 긴 강의 길이
    right = sum(lectures) # 최대 블루레이 크기는 모든 강의 길이의 합
    
    while left <= right:
        mid = (left + right) // 2
        cur_sum = 0
        cnt_blueray = 0
        
        # 강의 하나씩 더해가며 블루레이에 담을 수 있는지 여부 판단
        for i in range(N):
            if cur_sum + lectures[i] > mid: # 블루레이 하나더 필요
                cnt_blueray += 1
                cur_sum = lectures[i] # 새로운 블루레이에 강의[i] 담음.
            else:
                cur_sum += lectures[i] # 기존 블루레이에 강의[i] 담음.
        
        # 마지막에 남아 있는 강의 있으면 그것도 담아야하니까 
        if cur_sum != 0:
            cnt_blueray += 1
        
        # M개를 넘으면 안되니까 더 큰 값으로 나누도록 오른쪽 확인
        if cnt_blueray > M:
            left = mid + 1
        # 좀 더 작은 값도 가능한가 확인 => 최소 블루레이 크기 값 찾기위해
        else:
            right = mid - 1
    # 최소 가능한 블루레이 크기
    return left

print(binary_search(N, M, lectures))    