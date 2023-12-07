from collections import Counter

with open('input.txt') as input:
    lines = input.read().splitlines()


def camel_cards():
    hands = []
    card_vals = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    for idx, line in enumerate(lines):
        cards, bid = line.split(' ')
        card_val = [card_vals.index(c) for c in cards]
        c = Counter(cards).most_common()
        if c[0][1] == 5:
            hand_val = 6
        elif c[0][1] == 4:
            hand_val = 5
        elif c[0][1] == 3 and c[1][1] == 2:
            hand_val = 4
        elif c[0][1] == 3:
            hand_val = 3
        elif c[0][1] == 2 and c[1][1] == 2:
            hand_val = 2
        elif c[0][1] == 2:
            hand_val = 1
        else:
            hand_val = 0

        hands.append((hand_val, *card_val, bid))

    return sum([(idx+1) * int(x[-1]) for idx, x in enumerate(sorted(hands))])


def jokers_wild():
    hands = []
    card_vals = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    for idx, line in enumerate(lines):
        cards, bid = line.split(' ')
        card_val = [card_vals.index(c) for c in cards]
        counts = Counter(cards)
        joker_count = counts['J']
        if joker_count != 5:
            del counts['J']
        c = counts.most_common()
        if joker_count != 5:
            c[0] = (c[0][0], c[0][1] + joker_count)
        if c[0][1] == 5:
            hand_val = 6
        elif c[0][1] == 4:
            hand_val = 5
        elif c[0][1] == 3 and c[1][1] == 2:
            hand_val = 4
        elif c[0][1] == 3:
            hand_val = 3
        elif c[0][1] == 2 and c[1][1] == 2:
            hand_val = 2
        elif c[0][1] == 2:
            hand_val = 1
        else:
            hand_val = 0

        hands.append((hand_val, *card_val, bid))

    return sum([(idx+1) * int(x[-1]) for idx, x in enumerate(sorted(hands))])


print(f'Standard scoring: {camel_cards()}')
print(f'Jokers wild: {jokers_wild()}')
