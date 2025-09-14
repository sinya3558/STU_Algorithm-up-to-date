# https://school.programmers.co.kr/learn/courses/30/lessons/258712
def solution(friends, gifts):
    if not (2 <= len(friends) <= 50) or not (1 <= len(gifts) <= 10000):
        raise ValueError("Invalid input")

    n = len(friends)
    # 아.. enumerate()
    name_to_index = {name: i for i, name in enumerate(friends)}
    
    # init matrices & cnt
    gift_matrix = [[0] * n for _ in range(n)]  # gift_matrix[i][j]: i -> j
    given = [0] * n
    received = [0] * n
    
    # 아하 따로 빼내도 되는구나.  gift list 먼저 처리해두기. nested for loop 따로 써도 됬었네
    for g in gifts:
        a, b = g.split()
        i, j = name_to_index[a], name_to_index[b]   # dict uses key value as idx
        gift_matrix[i][j] += 1
        given[i] += 1
        received[j] += 1
    
    gift_status = [given[i] - received[i] for i in range(n)]    # 선물 지수
    result = [0] * n
    
    # compare all unique pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            if gift_matrix[i][j] > gift_matrix[j][i]:
                result[i] += 1
            elif gift_matrix[i][j] < gift_matrix[j][i]:
                result[j] += 1
            else:
                if gift_status[i] > gift_status[j]:
                    result[i] += 1
                elif gift_status[i] < gift_status[j]:
                    result[j] += 1
                # if its equal, nothing happens
    answer = max(result)
    return answer
