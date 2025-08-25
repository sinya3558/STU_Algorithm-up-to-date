from collections import deque

# deque 생성 및 초기화(initialize)
d = deque()

# add elements
d.append(1)     # 오른쪽 끝에 요소 추가
d.appendleft(2) # 왼쪽 끝에 요소 추가

# 요소 접근
print(d[0])     # 첫번째 요소 접근

# 요소 삭제
d.pop()         # 오른쪽 끝 요소 제거
d.popleft()     # 왼쪽 끝 요소 제거

# 요소 추가
d.extend([3, 4, 5])  # 오른쪽 끝에 여러 요소 추가
d.extendleft([0, 1]) # 왼쪽 끝에 여러 요소 추가

print(d)

# 회전
d.rotate(1)   # 오른쪽으로 1만큼 회전
print(f'rotation n=1: ',d)
d.rotate(-2)  # 왼쪽으로(음수라서) 2 만큼 회전
print(f'rotation n=-2: ',d)