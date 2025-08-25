# Test code 
def bin_sort_w_slicing(arr):
    arr[:] = [0]*arr.count(0) + [1]*arr.count(1)

def bin_sort_w_two_pointers(arr):
    ''' sorting a binary array in ascending order
    Argument type:
        arr(list[int]) : an array only contains 0 and 1
    Return type:
        None : just sorting the input array
    '''
    # 근데 python 에 포인터 없지 않나
    left_idx = 0
    right_idx = len(arr) - 1
    while left_idx < right_idx:
        while left_idx < len(arr) - 1 and arr[left_idx] == [0]:
            left += 1
        while right_idx >= 0 and arr[right_idx] == [1]:
            right_idx -= 1
        if left_idx < right_idx:
            arr[left_idx] = 0
            arr[right_idx] = 1
            left_idx = left_idx + 1
            right_idx = right_idx - 1
    '''
    left: int = 0
    right: int = len(arr) - 1
    while left < right:
        while left < len(arr) and arr[left] == 0:
            left += 1
        while right >= 0 and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = 0, 1
            left, right = left + 1, right - 1
    '''

for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 0, 1]):  
    bin_sort_w_two_pointers(arr)  
    print(arr)