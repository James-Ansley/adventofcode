class Board:
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.matches = [[False] * self.width for _ in range(self.height)]
        self.last_number = 0

    def check_number(self, number):
        self.last_number = number
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == number:
                    self.matches[i][j] = True

    def check_win(self):
        return (any(all(row) for row in self.matches) or
                any(all(col) for col in zip(*self.matches)))

    def sum_score(self):
        match_sum = 0
        for i in range(self.width):
            for j in range(self.height):
                if not self.matches[i][j]:
                    match_sum += int(self.board[i][j])
        return match_sum


with open('input_files/day04') as f:
    numbers, *boards = f.read().rstrip().split('\n\n')

numbers = [int(num) for num in numbers.split(',')]

boards = [[line.split() for line in board.split('\n')] for board in boards]
boards = [[[int(elt) for elt in line] for line in board] for board in boards]
boards = [Board(board) for board in boards]

winners = []
for number in numbers:
    for i in range(len(boards) - 1, -1, -1):
        boards[i].check_number(number)
        if boards[i].check_win():
            winners.append(boards[i])
            boards.pop(i)

first = winners[0]
last = winners[-1]
print(first.sum_score() * first.last_number)
print(last.sum_score() * last.last_number)
