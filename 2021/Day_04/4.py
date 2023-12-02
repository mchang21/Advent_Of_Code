PATH = '../Advent_Of_Code/2021/Day_04/'

# part one
def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().split("\n\n")
        numbers = [int(num) for num in data[0].split(',')]
        boards = []
        for card in data[1:]:
            rows = card.split('\n')
            board = [[int(num) for num in row.split()] for row in rows]
            boards.append(board)
    return numbers, boards

def mark_num(board, num):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == num:
                board[i][j] = -1
    return

def check_win(board):
    n = len(board)
    # simultaneously check i-th row and col
    for i in range(n):
        row_sum, col_sum = 0, 0
        for j in range(n):
            row_sum += board[i][j] if board[i][j] == -1 else 0
            col_sum += board[j][i] if board[j][i] == -1 else 0
        if row_sum == -5 or col_sum == -5:
            return True
    return False

def calculate_score(board):
    n = len(board)
    score = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1:
                score += board[i][j]
    return score

def calculate_winning_score(numbers, boards):
    n = len(boards[0])
    # iterate each number being drawn
    for num in numbers:
        # iterate over each bingo board
        for board in boards:
            mark_num(board, num)
            # check if board won
            if check_win(board):
                return calculate_score(board) * num

# part one
numbers, boards = parse_data(PATH + 'input.txt')
print(f"The score of the winning bingo board is: {calculate_winning_score(numbers, boards)}")

# part two
def calculate_last_winning_score(numbers, boards):
    total_boards, n = len(boards), len(boards[0])
    boards_won = set()
    # iterate each number being drawn
    for num in numbers:
        # iterate over each bingo board
        for i, board in enumerate(boards):
            # skip board that has won already
            if i in boards_won: continue
            mark_num(board, num)
            # check if board won
            if i not in boards_won and check_win(board):
                boards_won.add(i)
                # calculate the score of the last winning board
                if len(boards_won) == total_boards:
                    return calculate_score(board) * num

# part two
print(f"The score of the last winning bingo board is: {calculate_last_winning_score(numbers, boards)}.")