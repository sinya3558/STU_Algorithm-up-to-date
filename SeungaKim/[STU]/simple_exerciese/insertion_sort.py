# insertion sort
deck = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# what you need is (1) first element and (2) second element to compare with
for f in range(len(deck)):  # f as first ele
    # for s in range(f + 1, len(deck)):   # s as second element
    for s in range(f, 0, -1):    # checking elements in backward  # starting point should be f, not (f+1)
        if deck[s] < deck[s-1] : # 아.. 첫 번째(=정렬 끝난) 원소(들)은 가만히 두고, 정렬 안된 애들끼리 비교하는 거였음! ㅇㅋ
            # 앞에 애가 더 크면, 오른쪽으로 삽입
            deck[s - 1], deck[s] = deck[s], deck[s - 1]
        else:
            break
print(deck)

#         if deck[f] > deck[s]:       # when the first is greater than the second, move to left
#             deck[s], deck[f] = deck[f], deck[s]
#         else:
#             break   # otherwise, stay as it is
# print(deck)
