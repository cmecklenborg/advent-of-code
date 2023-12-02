import re

with open('input.txt') as input:
    lines = input.read().splitlines()


game_sum = 0
game_pow = 0

for line in lines:
    game, record = line.split(': ')
    p = True
    red_min, green_min, blue_min = 0, 0, 0
    pulls = record.split('; ')
    for pull in pulls:
        rgb = re.findall(r'(\d+) (\w+)', pull)
        for num_str, color in rgb:
            num = int(num_str)
            if color == 'red':
                red_min = max(red_min, int(num))
                p = p and num <= 12
            elif color == 'green':
                green_min = max(green_min, int(num))
                p = p and num <= 13
            elif color == 'blue':
                blue_min = max(blue_min, int(num))
                p = p and num <= 14

    if p:
        game_sum += int(game.split(' ')[-1])

    game_pow += red_min * green_min * blue_min

print(f'Part 1: {game_sum}')
print(f'Part 2: {game_pow}')
