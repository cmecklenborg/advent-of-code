with open('input.txt') as f:
    lines = f.read().splitlines()

trees = []
for line in lines:
    trees.append([int(x) for x in line])

visible = len(trees) * 2 + len(trees[0]) * 2 - 4

for row in range(1, len(trees)-1):
    for col in range(1, len(trees[0])-1):
        tree = trees[row][col]
        if tree > max(trees[row][:col]):
            visible += 1
            continue
        if tree > max(trees[row][col+1:]):
            visible += 1
            continue
        if tree > max([trees[y][col] for y in range(row)]):
            visible += 1
            continue
        if tree > max([trees[y][col] for y in range(row+1, len(trees))]):
            visible += 1
            continue

print(visible)
