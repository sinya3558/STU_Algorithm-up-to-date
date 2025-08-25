# binary search w recursive func

def bs(arr, target, start, end) :
    '''
    parameters
        - arr : sorted list that we can do binary search
        - target : target data we want to find
        - start : starting point of bs
        - end : ending poin tof bs
    rt_val
        - bs(arr, target, s, e) : updated bs() function for recursive call
    '''
    if start > end :    # boundary case?
        return None
    mid = (start + end) // 2    # no floating point, integer only
    
    # case 1 : when we find the target, return its index
    if arr[mid] == target:
        return mid
    # case 2: when mid > target, exlcude the mid point and search left side only
    elif arr[mid] > target:
        # update mid, start, end points
        return bs(arr, target, start, mid - 1)
    # case 3: otherwise, when mid < target, only search the right
    else :
        # update values
        return bs(arr, target, mid + 1, end)

# test input
num_elements, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

# test ouput
outcome = bs(arr, target, 0, num_elements - 1)
print(outcome + 1) # idx + 1
print(f'your target is located at', outcome, 'th index of the array')