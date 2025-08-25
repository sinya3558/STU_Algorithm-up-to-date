# Binary search : 떡 길이 지정하기
'''
- 오늘은 떡볶이 떡을 만드는 날. 떡볶이의 떡의 길이가 일정하지 x. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춤
    - 절단기에 높이(H) 를 지정하면 줄지어진 떡을 한 번에 절단.
        - 높이 H 보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 X
- 19, 14, 10, 17cm인 떡이 나란히 있고, 절단기의 높이가 15cm 라 하면, 자른 뒤 떡의 높이는 15, 14, 10, 15cm. 잘린 떡의 길이는 차례대로 4, 0, 0, 2 cm. 즉 손님은 6cm 만큼의 길이를 가짐
- 손님이 왔을 때, 요청한 총 길이가 M 일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 구하는 프로그램을 작성

- input
    - 첫째 줄에 떡의 개수 N 과 요청한 떡의 길이 M (1 ≤ N ≤ 1000000, 1 ≤ M ≤ 2000000000)
    - 둘째 줄에 떡의 개별 높이. 떡 높이의 총 합은 항상 M. 손님은 필요한 양만큼 떡을 사갈 수 있음.
- output
    - 적어도 M 만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값 출력
- 입출력 예시
    4 6
    19 15 10 17
    
    15
'''
# 1. 아이디어
'''
- 뒤에서부터 1cm 씩 자른거 더해서 M 이랑 일치하면 리턴하면 안되나 -> 조건 만족 yes or no?
- start 0, end = 18, mid = 9
'''

# user input
n, m = map(int, input().split())
list_t = list(map(int, input().split()))
# print(n, m, list_t)
# set up start, end points
start = 0
end = max(list_t)

outcome = 0 # init result 
while(start <= end):
    total_M = 0
    mid = (start + end) // 2
    for i in list_t:
        if i > mid :    # right side only (bigger than mid rice cake)
            total_M += i - mid
            
    if total_M < m:
        end = mid - 1
    else:
        outcome = mid
        start = mid + 1
        
print(outcome)