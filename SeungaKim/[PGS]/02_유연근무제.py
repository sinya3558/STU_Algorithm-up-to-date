'https://school.programmers.co.kr/learn/courses/30/lessons/388351'
# 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다. -> 시간 따로 지정해줘야하나?

def to_minutes(hhmm: int) -> int:
    ''' 시간 인풋 분 단위로 변환'''
    h, m = divmod(hhmm, 100)
    return h * 60 + m

def solution(schedules, timelogs, startday):
    '''
    schedules = 1d int array, n명이 설정한 출근시간
    timelogs = 2d int array, 일주일치 출근 시각 저장 리스트
    startday =  int, 요일(1 = monday... 7=sunday)
    rt_val =  상품 받을 직원 수
    '''
    if not (1 <= len(schedules) <= 1000):
        raise ValueError("invalid input(schedules)")
    if not (1 <= len(timelogs) <= 1000):
        raise ValueError("invalid timelogs")
    if not (1 <= startday <= 7):    
        raise ValueError("invalid day")
    
    answer = 0
    n = len(schedules)
    # acceptable_time = []
    # acceptable_time = schedules[i]+ 10
    
    for i in range(n):
        is_valid = True
        if not 700 <= schedules[i] <= 1100:
            raise ValueError("invalid starting time")
        # reset time every single loop
        acceptable_time = to_minutes(schedules[i]) + 10

        for j in range(7):
            weekday = (startday + j - 1) % 7 + 1
            if weekday <= 5:
                actual_time = to_minutes(timelogs[i][j])
                if actual_time > acceptable_time:
                    is_valid = False
                    break

        if is_valid:
            answer += 1
    return answer