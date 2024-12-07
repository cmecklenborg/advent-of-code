file = 'input.txt'

with open(file) as input:
    lines = input.read().splitlines()


def part_1():
    safe = 0

    for line in lines:
        report = [int(x) for x in line.split()]
        diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
        inc = all(d < 4 for d in diffs) and all(d > 0 for d in diffs)
        dec = all(d > -4 for d in diffs) and all(d < 0 for d in diffs)
        if inc or dec:
            safe += 1
    return safe


def part_2():
    safe = 0

    for line in lines:
        report = [int(x) for x in line.split()]
        diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
        inc = all(d < 4 for d in diffs) and all(d > 0 for d in diffs)
        dec = all(d > -4 for d in diffs) and all(d < 0 for d in diffs)
        if inc or dec:
            safe += 1
    return safe


print(f'Part 1: {part_1()}')
