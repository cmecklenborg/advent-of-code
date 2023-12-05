from collections import defaultdict
import re

with open('input.txt') as input:
    lines = input.read().splitlines()

syms = '!@#$%^&*()_+-=|:;/?'
x_max = len(lines[0])
y_max = len(lines)
parts = []
gears = defaultdict(list)

for y, line in enumerate(lines):
    nums = digits = re.finditer(r'\d+', line)

    for num in nums:
        is_part = False
        num_start = num.start()
        num_end = num.end()-1

        y_range = range(max(0, y-1), min(y_max-1, y+1)+1)
        x_range = range(max(0, num_start-1), min(x_max-1, num_end+1)+1)
        for xs in x_range:
            for ys in y_range:
                if lines[ys][xs] in syms:
                    is_part = True
                if lines[ys][xs] == '*':
                    gears[(ys, xs)].append(int(num.group()))

        if is_part:
            parts.append(int(num.group()))


gear_ratio = sum([gear[0] * gear[1] for gear in gears.values() if len(gear) == 2])

print(f'Parts sum: {sum(parts)}')
print(f'Gear ratios: {gear_ratio}')
