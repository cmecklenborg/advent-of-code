with open('input.txt') as f:
    bingos = f.readline().strip().split(',')
    board_lines = f.read().splitlines()

board_num = 0
boards = {}

for line in board_lines:
    if line == '':
        board_num += 1
        row = 0
        boards[board_num] = []
    else:
        boards[board_num].append(line.split())

winning_boards = []

for bingo in bingos:

    for board_key in boards.keys():
        if board_key in winning_boards:
            continue
        board = boards[board_key]

        # Mark off number
        for row in board:
            for idx, num in enumerate(row):
                if num == bingo:
                    row[idx] = None

        # Check if we have a bingo
        found_bingo = False
        for row in board:
            if row.count(None) == len(row):
                found_bingo = True

        for idx in range(5):
            col = [row[idx] for row in board]
            if col.count(None) == len(col):
                found_bingo = True

        if found_bingo:
            bingo_sum = sum([int(x) for row in board for x in row if x])
            print(bingo_sum*int(bingo))
            winning_boards.append(board_key)
