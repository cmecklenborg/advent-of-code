from statistics import median

with open('resources/day_10.txt') as f:
    lines = f.read().splitlines()

close_chars = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
pts = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

open_chars = ['(', '[', '{', '<']
scores = []
incomplete_lines = []

for line in lines:
    chunk = []
    skip_line = False
    for c in line:
        if skip_line:
            break

        if c in open_chars:
            chunk.append(c)
        elif close_chars[c] == chunk[-1]:
            chunk.pop()
        else:
            skip_line = True
            break

    if not skip_line:
        incomplete_lines.append(chunk)

for line in incomplete_lines:
    score = 0
    for c in line[::-1]:
        score *= 5
        score += pts[c]

    scores.append(score)

print(median(scores))
