# https://school.programmers.co.kr/learn/courses/30/lessons/258712
'''
두 사람이 서로 주고받은 기록이 있으면, 더 많이 준 사람이 다음 달 선물 1 +
만약 주고받은 수가 같거나 기록이 없으면, 선물 지수가 더 큰 사람이 선물 1개 +
선물 지수 = given - taken. if the same 선물 지수, nothing happens.
rt_val : 가장 많이 받는 친구의 선물 수

[제한 조건]
- 2 ≤ friends의 길이 = 친구들의 수 ≤ 50
friends의 원소는 친구의 이름을 의미하는 알파벳 소문자로 이루어진 길이가 10 이하인 문자열입니다.
이름이 같은 친구는 없습니다.
- 1 ≤ gifts의 길이 ≤ 10,000
gifts의 원소는 "A B"형태의 문자열입니다. A는 선물을 준 친구의 이름을 B는 선물을 받은 친구의 이름을 의미하며 공백 하나로 구분됩니다.
A와 B는 friends의 원소이며 A와 B가 같은 이름인 경우는 존재하지 않습니다. -> identical
'''
def solution(friends, gifts):
    if not (2 <= len(friends) <= 50):
        raise ValueError("invalid len of friends")
    if not(1 <= len(gifts) <= 10000):
        raise ValueError("invalid len of gifts")
    answer = 0
    fri_map = {name: idx for idx, name in enumerate(friends)}
    nums = len(friends)
    # calculate given - takers
    gift_cnt = [[0] * nums in len(friends)]
    given = [0] * nums
    taken = [0] * nums

    for g in gifts:
        a, b = g.split()    # A, B are seperated by blank
        g_idx = fri_map(a)  # idx for giver
        t_idx = fri_map(b)  # idx for taker
        gift_cnt[g_idx][t_idx] += 1
        given[g_idx] += 1
        taken[t_idx] += 1

    # cal 선물지수
    gift_index = [given[i] - taken[i] for i in range(len(friends))]
    num_friends = len(friends)
    next_month = [0]* len(friends)

    for i in range(len(num_friends)):
        for j in range(i + 1, num_friends):
            # when its greater,
            if gift_cnt[i][j] > gift_cnt[j][i]:
                next_month[i] += 1
            # when its smaller
            elif gift_cnt[i][j] < gift_cnt[j][i]:
                next_month[j] += 1
            # nothing happens if they've got the same 선물지수
    answer = max(next_month)
    return answer