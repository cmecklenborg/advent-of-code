from collections import Counter

file = 'input.txt'

with open(file) as input:
    lines = input.read().splitlines()

left, right = [], []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))


def part_1():
    left.sort()
    right.sort()

    return sum([abs(x - y) for x, y in zip(left, right)])


def part_2():
    cr = Counter(right)

    return sum([x*cr[x] for x in left])


print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')
