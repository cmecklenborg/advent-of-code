from collections import defaultdict

file = 'input.txt'
with open(file) as input:
    line = input.readline()

values = []
steps = line.split(',')
boxes = defaultdict(list)


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

        box = hash(label)
        lens = (label, num)
        if op == '-':
            for idx, bl in enumerate(boxes[box]):
                if bl[0] == label:
                    boxes[box].pop(idx)
                    break
        else:
            added = False
            for idx, bl in enumerate(boxes[box]):
                if bl[0] == label:
                    boxes[box][idx] = lens
                    added = True
                    break
            if not added:
                boxes[box].append(lens)

    power = 0
    for box, lenses in boxes.items():
        power += sum([(box + 1) * (idx+1) * int(lens[1]) for idx, lens in enumerate(lenses)])

    print(f'Focal power: {power}')


part_1(steps)
part_2(steps)
