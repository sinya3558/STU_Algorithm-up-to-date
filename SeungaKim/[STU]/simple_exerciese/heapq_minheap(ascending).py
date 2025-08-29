# Heap sort (ascending order)
import heapq
# default : min heap -> so you dont really need to sorting algorithm

def heapsort_min(iterable):
    h = []
    result = []
    # push all of elements to the heap, h
    for value in iterable:
        heapq.heappush(h, value)    # heappush : heap's append()
    # check out all elements of the heap(h) in order
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

iter = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
output = heapsort_min(iter)
print(output)