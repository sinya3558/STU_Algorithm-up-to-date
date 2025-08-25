# # Quick sort exercise
'''
num = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(num, start, end) :
    # 
    # parameters
    #     num : data set(list)
    #     start : starting point index(int), first element or pivot in htis case
    #     end : ending point (int)

    # rt_val:
    #     none
    # 
    if start >= end:
        return
    # set the pivot
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 왼쪽에서 부터 피벗 데이터보다 큰 데이터 찾기
        while(left <= end and num[pivot] >= num[left]): # pivot 보다 작으면, 패스한다
            left += 1
        # 오른쪽부터 피벗 데이터랑 비교해서 작은 데이터 찾기, start = 0
        while(right > start and num[pivot] <= num[right]): #pivot 보다 크면, 넘기고 오른쪽으로 패스
            right -= 1      # 오른쪽으로 이동
        if(left > right):   # 두 데이터가 서로 엇갈린 경우,
            # pivot 이랑 right 값(작은값) 교환한다
            # pivot = right
            # right = pivot
            # 이 아니고.. 얜 인덱스라고 제발 좀 챙겨 제발제발
            num[pivot], num[right] = num[right], num[pivot]
        # 아니라면, 원래 로직대로 크고 작은 데이터 두개 교환한다    $ 아하 여기서 교환해도 되는구나
        else:
            num[left], num[right] = num[right], num[left]
    # 재귀적으로 반복해서 pivot 기준으로 왼쪽 구간 / 오른쪽 구간 각각 정렬 해준다
    # 왼쪽
    quick_sort(num, start, right - 1)
    # 오른쪽
    quick_sort(num, right + 1, end) # 마지막에 pivot이랑 right 교환하니까? 그래서 pivot 값이 중간에 있어서?

quick_sort(num, 0, len(num)-1)
print(num)
'''

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_lc(arr):    # quick sort w/ list comprehension
	# 원소가 하나만 있으면 그냥 그대로 끝
	if len(arr) <= 1:
		return arr
	# set up pivot	
	pivot = arr[0]
	tail = arr[1:]   # pivot 제외한 리스트의 원소들 지정! list comprehension
	
	left_side = [x for x in tail if x <= pivot]   # pivot 보다 작은 데이터들 pivot 기준 왼쪽으로 정렬
	right_side = [x for x in tail if x > pivot]   # pivot 보다 큰 애들 pivot 기준 오른쪽으로 정렬!
	
	# 분할 이후, 중간 기준점 중심으로 왼쪽 오른족 각각 정렬 수행
	return quick_sort_lc(left_side) + [pivot] + quick_sort_lc(right_side)   # 근데 pivot 왜 저렇게 쓰지?
	
print(quick_sort_lc(arr))  # 오와 완전 심플하다잉