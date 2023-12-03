import re

with open('input.txt') as input:
    lines = input.read().splitlines()

game_sum = 0
syms = '!@#$%^&*()_+-=|:;/?'
x_max = len(lines[0])
y_max = len(lines)

for y, line in enumerate(lines):
    nums = digits = re.finditer(r'\d+', line)

    for num in nums:
        part = False
        num_start = num.start()
        num_end = num.end()-1

        y_range = range(max(0, y-1), min(y_max-1, y+1)+1)
        x_range = range(max(0, num_start-1), min(x_max-1, num_end+1)+1)
        for xs in x_range:
            for ys in y_range:
                if lines[ys][xs] in syms:
                    part = True

        if part:
            game_sum += int(num.group())

print(game_sum)
