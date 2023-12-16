from collections import defaultdict

file = 'input.txt'
with open(file) as input:
    line = input.readline()

values = []
steps = line.split(',')
boxes = defaultdict(dict)


def hash(input: str) -> int:
    curr_value = 0
    for c in input:
        curr_value += ord(c)
        curr_value *= 17
        curr_value = curr_value % 256
    return curr_value


def part_1(steps):
    for step in steps:
        values.append(hash(step))

    print(f'Hash sum: {sum(values)}')


def part_2(steps):
    for step in steps:
        if '=' in step:
            op = '='
            label, num = step.split('=')
        else:
            op = '-'
            label, num = step.split('-')

        box = boxes[hash(label)]
        if op == '-':
            if label in box:
                del box[label]
        else:
            box[label] = num

    power = 0
    for box, lenses in boxes.items():
        power += sum([(box + 1) * (slot + 1) * int(lens) for slot, lens in enumerate(lenses.values())])

    print(f'Focal power: {power}')


part_1(steps)
part_2(steps)
