from collections import defaultdict


with open('input.txt') as f:
    lines = f.read().splitlines()

boxes = defaultdict(list)

num_idx = [i for i, l in enumerate(lines) if ' 1   2' in l][0]

for row in range(num_idx-1, -1, -1):
    for col, c in enumerate(lines[row][1::4]):
        if c != ' ':
            boxes[col].append(c)

for line in lines[num_idx+2:]:
    _, num, _, src, _, dest = line.split()
    num, src, dest = int(num), int(src)-1, int(dest)-1
    boxes[dest] += boxes[src][-num:]
    del boxes[src][-num:]

print(boxes)

print(''.join([x[-1] for x in boxes.values()]))
