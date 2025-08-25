import heapq
nums = [4, 1, 7, 3, 8, 5]
# 1
heapq.heapify(nums)       # nums 이제 힙이 됨
# 2
heapq.heappush(nums, 2)   # 2를 힙에 추가
# 3
print(heapq.heappop(nums))       # 1 제거하고 반환
# 4
print(heapq.heappushpop(nums, 6)) # 6 추가 후, 가장 작은 요소(2) 꺼내 반환
# 5
print(heapq.heapreplace(nums, 6)) # 가장 작은 요소(3) 꺼내 반환 후, 6 추가
print(f'current heap = ', nums) # 6 2개인지 체크
# 6
print(heapq.nlargest(3, nums))    # 가장 큰 요소 3개를 리스트로 반환([8, 7, 6])
# 7
print(heapq.nsmallest(2, nums))   # 가장 작은 요소 2개 리스트로 반환([4, 5])