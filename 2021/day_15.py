with open('resources/day_15.txt') as f:
    lines = f.read().splitlines()

grid = []

size = len(lines)*5

for line in lines:
    grid.append(
        [int(c) for c in line] +
        [int(c) + 1 for c in line] +
        [int(c) + 2 for c in line] +
        [int(c) + 3 for c in line] +
        [int(c) + 4 for c in line]
    )

big_grid = []

for idx in range(5):
    for line in grid:
        big_grid.append([x+idx for x in line])

for y in range(size):
    for x in range(size):
        if big_grid[y][x] > 9:
            big_grid[y][x] -= 9

cost = [[0 for _ in range(size)] for _ in range(size)]


def min_cost(cost):

    # Initialize first row
    for i in range(1, size):
        cost[0][i] = cost[0][i-1] + big_grid[0][i]

    # Initialize first column
    for i in range(1, size):
        cost[i][0] = cost[i-1][0] + big_grid[i][0]

    for i in range(1, size):
        for j in range(1, size):
            adjacent = [
                cost[i-1][j], cost[i][j-1],
            ]

            cost[i][j] = big_grid[i][j] + min(adjacent)

    for i in range(size):
        for j in range(size):
            adjacent = []

            if i < size-1:
                adjacent.append(cost[i+1][j])
            if j < size-1:
                adjacent.append(cost[i][j+1])
            if i > 0:
                adjacent.append(cost[i-1][j])
            if j > 0:
                adjacent.append(cost[i][j-1])

            cost[i][j] = big_grid[i][j] + min(adjacent)

    return cost[size-1][size-1]


print(min_cost(cost))
