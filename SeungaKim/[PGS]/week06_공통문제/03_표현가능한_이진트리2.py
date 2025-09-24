# 표현 가능한 이진트리(2023 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/150367

def is_valid(bits: str) -> bool:    ## bits(str, not int)
    if len(bits) <= 1:  # empty str or 길이 1이면 True 반환
        return True

    mid = len(bits) // 2
    root = bits[mid]

    left_child = bits[:mid]
    right_child = bits[mid + 1 :]

    if root == "0":
        if left_child and left_child[len(left_child) // 2] == "1":
            return False
        if right_child and right_child[len(right_child) // 2] == "1":
            return False

    # recursive calls for l n r
    return is_valid(left_child) and is_valid(right_child)


def solution(numbers):
    answer = []

    for num in numbers:
        binary = bin(num)[2:]
        length = 1

        while length < len(binary):
            length = length * 2 + 1

        binary = binary.zfill(length)
        answer.append(1 if is_valid(binary) else 0)

    return answer
