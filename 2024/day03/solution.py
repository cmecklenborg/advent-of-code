import re

file = "input.txt"

with open(file) as input:
    lines = input.read().splitlines()


def part_1():
    result = 0
    for line in lines:
        muls = re.findall(r"mul\(\d+,\d+\)", line)
        result += sum(
            [int(x) * int(y) for x, y in [re.findall(r"\d+", mul) for mul in muls]]
        )

    return result


print(f"Part 1: {part_1()}")
