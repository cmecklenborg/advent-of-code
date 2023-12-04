import re

with open('input.txt') as input:
    lines = input.read().splitlines()

points = 0
cards = {c: 1 for c in range(len(lines))}

for card, line in enumerate(lines):
    _, nums = line.split(': ')
    a, b = nums.split(' | ')
    win = re.findall(r'\d+', a)
    have = re.findall(r'\d+', b)

    matches = 0

    for w in win:
        if w in have:
            matches += 1

    if matches > 0:
        points += 2**(matches-1)
        for m in range(card + 1, card + matches + 1):
            cards[m] = cards[m] + cards[card]


print(f"Points: {points}")
print(f"Cards: {sum(cards.values())}")
