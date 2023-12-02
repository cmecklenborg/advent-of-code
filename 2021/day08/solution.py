with open('input.txt') as f:
    lines = f.read().splitlines()

count = 0

for line in lines:
    input = line.split(' | ')[0].split(' ')
    output = line.split(' | ')[1].split(' ')

    mapping = {}
    for code in input:
        # First the unique ones - 1/4/7/8
        if len(code) == 2:
            mapping[1] = code
        elif len(code) == 4:
            mapping[4] = code
        elif len(code) == 3:
            mapping[7] = code
        elif len(code) == 7:
            mapping[8] = code

    for code in input:
        # 0/6/9
        if len(code) == 6:
            if set(mapping[4]).issubset(set(code)):
                mapping[9] = code
            elif set(mapping[1]).issubset(set(code)):
                mapping[0] = code
            else:
                mapping[6] = code

    for code in input:
        # 2/3/5
        if len(code) == 5:
            if set(mapping[1]).issubset(set(code)):
                mapping[3] = code
            elif set(code).issubset(set(mapping[6])):
                mapping[5] = code
            else:
                mapping[2] = code

        pass

    out_str = ''
    for out in output:
        for k, v in mapping.items():
            if set(out) == set(v):
                out_str += str(k)

    count += int(out_str)

print(count)
