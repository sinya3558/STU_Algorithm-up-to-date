# Make a function to find max and sencond max values from the integer array( or list)
"""
input [3, -1, 5, 0, 7, 4, 9, 1]
output [9, 7]

input [7]
output [7]
"""

import sys

arr = []
nums_elements = int(input())    # how many elements in the array?
# ele = int(input())              # list up elements

for _ in range(nums_elements):
    ele = int(input())              # list up elements # 맞지 여기가 맞지 바보똥구리야
    arr.append(ele)                 
# print(arr)

def find_maxes(array):
    # parameters : a variable in the function definition
    # arguments : actual value passed to the function when its called
    '''
    Arguments:
        array(list) : a list of integers offered by a user
    Return:
        array(list) : [max value, second max value]
    '''
    # when its an empty array
    # if array  == []:
    #     return array
    if len(array) < 2 :
        return array
    max1, max2 = array[:2]
    if max2 > max1 :
        max1, max2 = max2, max1
    for n in arr[2:]:
        if n > max1:
            max2 = max1
            max1 = n

        elif n > max2:
            max2 = n

    return [max1, max2]

final_arr = find_maxes(arr)
print(final_arr)