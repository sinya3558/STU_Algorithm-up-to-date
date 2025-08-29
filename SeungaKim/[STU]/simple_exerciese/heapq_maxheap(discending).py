# sort heap in discending order by maxheap
import heapq

def heapsort_max(iterable):
    h = []
    result = []
    # push all iterable elements to the heap, h
    for value in iterable:
        heapq.heappush(h, -value)   # negative sign needed
        # print(h)    # discending, [-9, -7, -3, -1, -5, -2]
    
    # append elements of the heap in order (discending)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))    # why theres - sign @ heapq again -> result should be back to the positive
    return result

iter_2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
output_2 = heapsort_max(iter_2)
print(output_2)