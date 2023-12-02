with open('input.txt') as f:
    lines = f.read().splitlines()

heights = []
for line in lines:
    heights.append([int(x) for x in line])

max_y = len(heights)
max_x = len(heights[0])
basins = []

def process_basin(heights, basin, x, y):
    here = heights[y][x]
    if here is None or here == 9:
        return basin
    else:
        basin += 1

    heights[y][x] = None

    if y > 0:
        basin = process_basin(heights, basin, x, y-1)
    if y < max_y - 1:
        basin = process_basin(heights, basin, x, y + 1)
    if x > 0:
        basin = process_basin(heights, basin, x-1, y)
    if x < max_x - 1:
        basin = process_basin(heights, basin, x+1, y)

    return basin


for y in range(max_y):
    for x in range(max_x):
        basin = 0
        basin = process_basin(heights, basin, x, y)
        if basin:
            basins.append(basin)

basins.sort()
print(basins[-1]*basins[-2]*basins[-3])
