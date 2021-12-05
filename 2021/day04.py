class Board:
    def __init__(self, board):
        self.orthogonals = [{*row} for row in board]
        self.orthogonals += [{*col} for col in zip(*board)]
        self.last_number = 0

    def check_number(self, number):
        self.last_number = number
        for orthogonal in self.orthogonals:
            orthogonal.discard(number)

    def check_win(self):
        return not all(orthogonal for orthogonal in self.orthogonals)

    def sum_score(self):
        return sum(sum(orthogonal) for orthogonal in self.orthogonals) // 2


with open('input_files/day04') as f:
    numbers, *boards = f.read().rstrip().split('\n\n')

numbers = [int(num) for num in numbers.split(',')]

boards = [board.split('\n') for board in boards]
boards = [[[*map(int, row.split())] for row in board] for board in boards]
boards = [Board(board) for board in boards]

winners = []
for number in numbers:
    for i in range(len(boards) - 1, -1, -1):
        boards[i].check_number(number)
        if boards[i].check_win():
            winners.append(boards[i])
            boards.pop(i)

print(winners[0].sum_score() * winners[0].last_number)
print(winners[-1].sum_score() * winners[-1].last_number)
