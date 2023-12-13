from collections import defaultdict

file = 'input.txt'
with open(file) as input:
    lines = input.read().splitlines()

start_idx = 0
blanks = [idx for idx, line in enumerate(lines) if line == ''] + [len(lines)]

horz = defaultdict(int)
vert = defaultdict(int)
horz2 = defaultdict(int)
vert2 = defaultdict(int)

for pidx, blank in enumerate(blanks):
    pattern = lines[start_idx:blank]
    start_idx = blank + 1
    full_width = len(pattern[0])
    full_height = len(pattern)

    # Find vertical symmetry
    for x in range(1, full_width):
        pw = min(x, full_width - x)
        left = [p[x-pw:x] for p in pattern]
        right = [p[x+pw-1:x-1:-1] for p in pattern]
        if left == right:
            vert[pidx] = x
            break

    # Horizontal symmetry
    for y in range(1, full_height):
        ph = min(y, full_height - y)
        top = pattern[y-ph:y]
        bottom = pattern[y+ph-1:y-1:-1]
        if top == bottom:
            horz[pidx] = y
            break

    for sx in range(0, full_width):
        for sy in range(0, full_height):
            old_sym = pattern[sy][sx]
            new_sym = '#' if old_sym == '.' else '.'

            # Fix smudge
            pattern[sy] = pattern[sy][0:sx] + new_sym + pattern[sy][sx+1:]

            # Find vertical symmetry
            for x in range(1, full_width):
                pw = min(x, full_width - x)
                left = [p[x-pw:x] for p in pattern]
                right = [p[x+pw-1:x-1:-1] for p in pattern]
                if left == right and vert[pidx] != x:
                    vert2[pidx] = x
                    break

            # Horizontal symmetry
            for y in range(1, full_height):
                ph = min(y, full_height - y)
                top = pattern[y-ph:y]
                bottom = pattern[y+ph-1:y-1:-1]
                if top == bottom and horz[pidx] != y:
                    horz2[pidx] = y

            # Reset smudge
            pattern[sy] = pattern[sy][0:sx] + old_sym + pattern[sy][sx+1:]

print(f'Part 1 {100*sum(horz.values()) + sum(vert.values())}')
print(f'Part 2 {100*sum(horz2.values()) + sum(vert2.values())}')
