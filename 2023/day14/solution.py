from collections import defaultdict

file = 'sample.txt'
with open(file) as input:
    lines = input.read().splitlines()

round_rocks = []
cube_rocks = []

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        coords = (x, y)
        if c == '#':
            cube_rocks.append(coords)
        elif c == 'O':
            round_rocks.append(coords)
            # prev_round_rocks = [c[0] for c in round_rocks if c[1] == y]
            # prev_cube_rocks = [c[0] for c in cube_rocks if c[1] == y]
            # new_x = min([x, len(prev_round_rocks)] + prev_cube_rocks)
            # round_rocks.append((new_x, y))


# for col in range(0, len(lines[0])):
for col in range(0, 1):
    round_rows = [r[1] for r in round_rocks if r[0] == col]
    cube_rows = [c[1] for c in cube_rocks if c[0] == col]
    print(f'Round rows: {round_rows}')
    print(f'Cube rows: {cube_rows}')

print(round_rocks)
