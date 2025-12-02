file = "input.txt"

with open(file) as input:
    lines = input.read().splitlines()


def part_1():
    x = 50
    z = 0

    for line in lines:
        d = int(line[1:])
        x += d * (-1 if line[0] == "R" else 1)
        if x % 100 == 0:
            z += 1

    return z


def part_2():
    x = 50
    z = 0
    for line in lines:
        d = int(line[1:])
        sign = -1 if line[0] == "R" else 1
        for _ in range(d):
            x += sign
            if x % 100 == 0:
                z += 1
    return z


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
