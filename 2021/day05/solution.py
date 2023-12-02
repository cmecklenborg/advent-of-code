import re

with open('input.txt') as f:
    lines = f.read().splitlines()


all_vents = [[int(x) for x in re.split(',| -> ', line)] for line in lines]

size = max([x for vent in all_vents for x in vent]) + 1

grid = [[0 for x in range(size)] for y in range(size)]

for vent in all_vents:
    x1, y1, x2, y2 = vent
    # Vertical
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[y][x1] += 1
    # Horizontal or Diagonal
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m*x1
        # print(f"m: {m}, b: {b}, for x in range {min(x1, x2), max(x1, x2)+1}")
        for x in range(min(x1, x2), max(x1, x2)+1):
            y = int(m*x + b)
            grid[y][x] += 1

print(sum([1 for row in grid for x in row if x > 1]))
