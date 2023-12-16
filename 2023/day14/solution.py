file = 'input.txt'
with open(file) as input:
    rock_map = input.read().splitlines()


def roll_rocks(rock_map: list[str]) -> list[str]:
    for y, row in enumerate(rock_map):
        for x, c in enumerate(row):
            if c == 'O':
                obstacles = [y for y in range(y) if rock_map[y][x] in '#O']
                new_y = max(obstacles, default=-1) + 1
                if new_y != y:
                    rock_map[y] = f'{rock_map[y][:x]}.{rock_map[y][x+1:]}'
                    rock_map[new_y] = f'{rock_map[new_y][:x]}O{rock_map[new_y][x+1:]}'

    return rock_map


def load(rock_map: list[str]) -> int:
    max_y = len(rock_map)
    load = sum(row.count('O') * (max_y - y) for y, row in enumerate(rock_map))
    return load


roll_rocks(rock_map)
print(load(rock_map))
