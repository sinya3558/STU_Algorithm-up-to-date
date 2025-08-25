card_deck = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for c in range(len(card_deck)) :
    # c : current node (it might be the first element of the card_deck list)
    min_idx = c
    for s in range(c + 1, len(card_deck)):
        if card_deck[min_idx] > card_deck[s] :  # while sortin, if we find the smallest element,
            min_idx = s                         # update min_idx as s
        # otherwise,
        # swap their positions
        card_deck[min_idx], card_deck[c] = card_deck[c], card_deck[min_idx]
        # card_deck[c] = card_deck[min_idx]

print(card_deck)