file = 'input.txt'
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

load = 0
max_x = len(lines[0])
max_y = len(lines)
for col in range(0, max_x):
    round_rows = [r[1] for r in round_rocks if r[0] == col]
    cube_rows = [c[1] for c in cube_rocks if c[0] == col]
    cube_rows.insert(0, -1)

    for ridx in range(1, len(cube_rows)):
        round_count = sum([1 for rr in round_rows if rr > cube_rows[ridx-1] and rr < cube_rows[ridx]])
        round_rows = round_rows[round_count:]
        load += sum([max_y - 1 - x - cube_rows[ridx-1] for x in range(0, round_count)])

    load += sum([max_y - 1 - x - cube_rows[-1] for x in range(0, len(round_rows))])
    
print(load)
