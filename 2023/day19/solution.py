file = 'sample.txt'
with open(file) as input:
    lines = input.read().splitlines()


def follow_workflow(part):
    x, m, a, s = part['x'], part['m'], part['a'], part['s']
    key = 'in'
    while key not in ['A', 'R']:
        workflow = workflows[key]
        for step in workflow:
            if eval(step[0]):
                key = step[1]
                break

    return key


workflows = {}

for idx, line in enumerate(lines):
    if line == '':
        break

    name, workflow = line[0:-1].split('{')
    steps = []
    for step in workflow.split(','):
        if ':' in step:
            steps.append(tuple(step.split(':')))
        else:
            steps.append(('True', step))
    workflows[name] = steps


def part_1():
    ratings = 0
    for line in lines[idx+1:]:
        part = {}
        for p in line[1:-1].split(','):
            exec(p, part)

        key = follow_workflow(part)
        if key == 'A':
            rating = sum([part['x'], part['m'], part['a'], part['s']])
            ratings += rating

    print(f'Part ratings: {ratings}')


part_1()
