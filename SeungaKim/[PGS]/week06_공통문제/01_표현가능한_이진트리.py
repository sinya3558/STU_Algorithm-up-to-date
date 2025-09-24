# 표현 가능한 이진트리(2023 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/150367

class Node:
    def __init__(self, data="0"):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, bits):
        self.root = self.build_binary_tree(bits)

    def build_binary_tree(self, bits):
        if not bits:
            return None

        mid = len(bits) // 2
        node = Node(bits[mid])
        node.left = self.build_binary_tree(bits[:mid])
        node.right = self.build_binary_tree(bits[mid + 1 :])
        return node

    def is_valid(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return True

        # if its dummy = 0, otherwise = 1
        if node.data == "0":
            if node.left and node.left.data == "1":
                return False
            if node.right and node.right.data == "1":
                return False

        return self.is_valid(node.left) and self.is_valid(node.right)


def solution(numbers):
    answer = []

    for num in numbers:
        binary = bin(num)[2:]

        length = 1
        while length < len(binary):
            length = length * 2 + 1

        binary = binary.zfill(length)
        tree = Tree(binary)

        if tree.is_valid():
            answer.append(1)
        else:
            answer.append(0)
    return answer

# test input
print(solution([7, 42, 5])) # 왜 안되냐 또!!!!!!