from collections import defaultdict
from functools import cache


file = 'sample.txt'
with open(file) as input:
    lines = input.read().splitlines()

max_x = len(lines[0])
max_y = len(lines)
loss = [[None for x in range(0, max_x)] for y in range(max_y)]
path = [[None for x in range(0, max_x)] for y in range(max_y)]
loss[0][0] = 0
path[0][0] = ('E', 0)


def new_path(prev_path: tuple, dir: str) -> tuple:
    return (dir, 1) if prev_path[0] != dir else (dir, prev_path[1] + 1)


for x in range(max_x):
    for y in range(max_y):
        if x == 0 and y == 0:
            continue
        neighbors = []
        dirs = []
        if x > 0 and loss[y][x-1] is not None:
            prev_path = path[y][x-1]
            if prev_path != ('E', 3):
                neighbors.append(loss[y][x-1])
                dirs.append(new_path(prev_path, 'E'))
        if x < max_x - 1 and loss[y][x+1] is not None:
            prev_path = path[y][x+1]
            if prev_path != ('W', 3):
                neighbors.append(loss[y][x+1])
                dirs.append(new_path(prev_path, 'W'))
        if y > 0 and loss[y-1][x] is not None:
            prev_path = path[y-1][x]
            if prev_path != ('S', 3):
                neighbors.append(loss[y-1][x])
                dirs.append(new_path(prev_path, 'S'))
        if y < max_y - 1 and loss[y+1][x] is not None:
            prev_path = path[y+1][x]
            if prev_path != ('N', 3):
                neighbors.append(loss[y+1][x])
                dirs.append(new_path(prev_path, 'N'))

        if neighbors:
            min_loss = min(zip(neighbors, dirs))
            # print(f'Min loss: {min_loss}')
            loss[y][x] = int(lines[y][x]) + min_loss[0]
            path[y][x] = min_loss[1]

print(loss)
# print(path)
