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


def part_2():
    result = 0
    do = True
    for line in lines:
        muls = re.findall(r"mul\(\d+,\d+\)", line)
        dos = re.findall(r"do[^n].*?mul\(\d+,\d+\)", line)
        donts = re.findall(r"don't.*?mul\(\d+,\d+\)", line)

        for mul in muls:
            if len(dos) > 0 and mul in dos[0]:
                do = True
                dos.pop(0)
            elif len(donts) > 0 and mul in donts[0]:
                do = False
                donts.pop(0)

            if do:
                x, y = re.findall(r"\d+", mul)
                result += int(x) * int(y)

    return result


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
