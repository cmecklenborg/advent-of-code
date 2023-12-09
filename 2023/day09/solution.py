import re


with open('input.txt') as input:
    lines = input.read().splitlines()


def extrap_forward() -> int:
    extrap = 0

    for line in lines:
        nums_0 = [int(x) for x in re.findall(r'-?\d+', line)]
        diffs = []
        nums = nums_0

        while (any(nums)):
            ln = len(nums)
            nums = [nums[i+1] - nums[i] for i in range(ln-1)]
            diffs.append(nums[-1])

        extrap += sum(diffs, nums_0[-1])

    return extrap


def extrap_back() -> int:
    extrap = 0

    for line in lines:
        nums = [int(x) for x in re.findall(r'-?\d+', line)]
        diffs = [nums]

        while (any(nums)):
            ln = len(nums)
            nums = [nums[i+1] - nums[i] for i in range(ln-1)]
            diffs.append(nums)

        line_val = 0
        for diff in diffs[::-1]:
            line_val = diff[0] - line_val

        extrap += line_val
    return extrap


print(extrap_forward())
print(extrap_back())
