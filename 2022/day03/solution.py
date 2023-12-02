with open('input.txt') as f:
    lines = f.readlines()

pri = 0

for idx in range(0, len(lines), 3):
    a = set(lines[idx].strip())
    b = set(lines[idx+1].strip())
    c = set(lines[idx+2].strip())

    common = a.intersection(b).intersection(c).pop()
    o = ord(common)
    val = o - 96 if o > 96 else o - 38
    pri += val

print(pri)
