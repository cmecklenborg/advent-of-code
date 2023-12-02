import re

with open('input.txt') as input:
    lines = input.read().splitlines()


def part_1():
    cal = 0

    for line in lines:
        digits = re.findall(r'\d', line)
        num = digits[0] + digits[-1]
        cal += int(num)

    return cal


def part_2():
    subs = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    keys = '|'.join(subs.keys())

    cal = 0

    for line in lines:

        s1 = re.search(f'(\d|{keys})', line)[0]
        s2 = re.search(f"(\d|{keys[-1::-1]})", line[-1::-1])[0][-1::-1]
        d1 = subs.get(s1, s1)
        d2 = subs.get(s2, s2)
        cal += int(d1 + d2)

    return cal


print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')
