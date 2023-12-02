with open('input.txt') as f:
    lines = f.read().splitlines()

coords = []

gap = lines.index('')

for line in lines[0:gap]:
    x, y = line.split(',')
    coords.append((int(x), int(y)))

folds = lines[gap+1:]

max_x = max([x[0] for x in coords]) + 1
max_y = max([x[1] for x in coords]) + 1

grid = [[0 for x in range(max_x)] for y in range(max_y)]

for coord in coords:
    x, y = coord
    grid[y][x] = 1

for fold in folds:
    fold_dir, fold_line = fold.split(' ')[-1].split('=')
    fold_line = int(fold_line)

    max_y = len(grid)
    max_x = len(grid[0])

    if fold_dir == 'y':
        new_grid = grid[0:fold_line]
        for y in range(1, max_y - fold_line):
            sum_line = [(x1 or x2) for x1, x2 in zip(grid[fold_line-y], grid[fold_line+y])]
            new_grid[fold_line-y] = sum_line
    else:
        new_grid = [line[0:fold_line] for line in grid]
        for y in range(max_y):
            for x in range(1, max_x - fold_line):
                new_grid[y][fold_line-x] = grid[y][fold_line-x] or grid[y][fold_line+x]

    grid = new_grid
    print(sum([sum(i) for i in grid]))

for line in grid:
    print(' '.join(line))
