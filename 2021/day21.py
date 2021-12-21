from functools import lru_cache


def play(p1, p2, s1=0, s2=0, dice=0):
    if s2 >= 1000:
        return 0, s1
    p1 += sum((dice + i) % 100 for i in (1, 2, 3))
    p1 %= 10
    s1 = s1 + p1 + 1
    rolls, score = play(p2, p1, s2, s1, (dice + 3) % 100)
    return rolls + 3, score


@lru_cache(maxsize=None)
def play_quantum(p1, p2, s1=0, s2=0):
    if s2 >= 21:
        return 0, 1
    win1, win2 = 0, 0
    for roll, n in (3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1):
        pos = (p1 + roll) % 10
        score = s1 + pos + 1
        p2_score, p1_score = play_quantum(p2, pos, s2, score)
        win1, win2 = win1 + p1_score * n, win2 + p2_score * n
    return win1, win2


with open('input_files/day21') as f:
    p1, p2 = (int(line[-2]) - 1 for line in f.readlines())

rolls, score = play(p1, p2)
print(rolls * score)

print(max(play_quantum(p1, p2)))
