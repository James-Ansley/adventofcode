from collections import deque
from itertools import islice

with open('../input_files/day22') as f:
    player1, player2 = f.read().split('\n\n')
    player1, player2 = player1.split('\n')[1:], player2.split('\n')[1:]
    player1, player2 = deque(map(int, player1)), deque(map(int, player2))

deck1, deck2 = deque(player1), deque(player2)

while deck1 and deck2:
    card1, card2 = deck1.popleft(), deck2.popleft()
    if card1 > card2:
        deck1.extend((card1, card2))
    else:
        deck2.extend((card2, card1))

score = sum(i * val for i, val in enumerate(reversed(deck1 + deck2), start=1))
print(score)


def play(deck1, deck2):
    previous_games = set()

    while deck1 and deck2:
        if (round := (tuple(deck1), tuple(deck2))) in previous_games:
            return deck1, 1
        previous_games.add(round)

        card1, card2 = deck1.popleft(), deck2.popleft()
        if len(deck1) > card1 and len(deck2) > card2:
            _, winner = play(deque(islice(deck1, card1)), deque(islice(deck2, card2)))
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            deck1.extend((card1, card2))
        else:
            deck2.extend((card2, card1))

    return deck1 + deck2, 1 if deck1 else 2


deck1, deck2 = deque(player1), deque(player2)
deck, _ = play(deck1, deck2)
score = sum(i * val for i, val in enumerate(reversed(deck), start=1))
print(score)
