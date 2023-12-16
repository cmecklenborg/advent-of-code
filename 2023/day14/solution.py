from functools import cache

file = 'input.txt'
with open(file) as input:
    rock_map = tuple(input.read().splitlines())


@cache
def roll_rocks(rock_map: tuple[str]) -> tuple[str]:
    rock_map = list(rock_map)
    for y, row in enumerate(rock_map):
        for x, c in enumerate(row):
            if c == 'O':
                obstacles = [y for y in range(y) if rock_map[y][x] in '#O']
                new_y = max(obstacles, default=-1) + 1
                if new_y != y:
                    rock_map[y] = f'{rock_map[y][:x]}.{rock_map[y][x+1:]}'
                    rock_map[new_y] = f'{rock_map[new_y][:x]}O{rock_map[new_y][x+1:]}'

    return tuple(rock_map)


def load(rock_map: tuple[str]) -> int:
    max_y = len(rock_map)
    load = sum(row.count('O') * (max_y - y) for y, row in enumerate(rock_map))
    return load


def part_1(rock_map):
    rock_map = roll_rocks(rock_map)
    print(f'Roll north: {load(rock_map)}')


@cache
def rotate(rock_map: tuple[str]) -> tuple[str]:
    return tuple(''.join(row) for row in zip(*rock_map[::-1]))


@cache
def thousand_cycles(rock_map: tuple[str]) -> tuple[str]:
    for _ in range(4 * 1000):
        rock_map = roll_rocks(rock_map)
        rock_map = rotate(rock_map)
    return rock_map


def part_2(rock_map):
    cycles = 1_000_000
    for _ in range(cycles):
        rock_map = thousand_cycles(rock_map)
    print(f'Spin cycle: {load(rock_map)}')


part_1(rock_map)
part_2(rock_map)
