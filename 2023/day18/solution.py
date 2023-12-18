import re


file = 'input.txt'
with open(file) as input:
    lines = input.read().splitlines()



def shoelace(trench: [int], perimeter: int) -> int:
    area = 0
    for idx in range(len(trench) - 1):
        x1, y1 = trench[idx]
        x2, y2 = trench[idx + 1]
        area += (x1 * y2 - x2 * y1)

    return (area + perimeter) // 2 + 1


def little_lagoon():
    trench = []
    x, y = 0, 0
    perimeter = 0
    for line in lines:
        dir, num_str, _ = line.split(' ')
        num = int(num_str)
        perimeter += num
        if dir == 'R':
            x  += num
        elif dir == 'L':
            x -= num
        elif dir == 'D':
            y += num
        elif dir == 'U':
            y -= num

        trench.append((x, y))

    dug = shoelace(trench, perimeter)

    print(f'Little Lagoon: {dug}')


def big_lagoon():
    trench = []
    x, y = 0, 0
    perimeter = 0
    for line in lines:
        code = re.search(r'#([\da-z]+)', line).group()
        num = int(code[1:-1], 16)
        dir = code[-1]
        perimeter += num
        if dir == '0':
            x  += num
        elif dir == '2':
            x -= num
        elif dir == '1':
            y += num
        elif dir == '3':
            y -= num

        trench.append((x, y))

    dug = shoelace(trench, perimeter)

    print(f'Big Lagoon: {dug}')


# little_lagoon()
big_lagoon()