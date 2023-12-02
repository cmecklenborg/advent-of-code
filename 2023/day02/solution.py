with open('input.txt') as input:
    lines = input.read().splitlines()


def part_1():
    game_sum = 0

    for line in lines:
        game, record = line.split(': ')
        p = True
        sets = record.split('; ')
        for s in sets:
            cubes = s.split(', ')
            for cube in cubes:
                num, color = cube.split(' ')
                if (color == 'red' and int(num) > 12) or color == 'green' and int(num) > 13 or (color == 'blue' and int(num) > 14):
                    p = False
                    break
        if p:
            game_sum += int(game.split(' ')[-1])

    return game_sum


def part_2():
    game_sum = 0

    for line in lines:
        _, record = line.split(': ')
        red_min, green_min, blue_min = 0, 0, 0
        sets = record.split('; ')
        for s in sets:
            cubes = s.split(', ')
            for cube in cubes:
                num, color = cube.split(' ')
                if color == 'red':
                    red_min = max(red_min, int(num))
                elif color == 'green':
                    green_min = max(green_min, int(num))
                elif color == 'blue':
                    blue_min = max(blue_min, int(num))
        game_sum += red_min * green_min * blue_min

    return game_sum


print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')
