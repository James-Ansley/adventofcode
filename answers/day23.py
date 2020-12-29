with open('../input_files/day23') as f:
    starting_cups = [int(c) for c in f.read()]


class Node:
    __slots__ = ['val', 'next']

    def __init__(self, val, next):
        self.val = val
        self.next = next


def run(cups, runs):
    hi = max(cups)
    nodes = [None] * hi
    tail = None
    for cup in reversed(cups):
        tail = Node(cup, tail)
        nodes[tail.val - 1] = tail
    nodes[cups[-1] - 1].next = tail

    current = nodes[cups[0] - 1]

    for _ in range(runs):
        c1 = current.next
        c2 = c1.next
        c3 = c2.next

        target = (current.val - 2) % hi
        while target in (c1.val - 1, c2.val - 1, c3.val - 1):
            target = (target - 1) % hi
        target = nodes[target]

        current.next = c3.next
        c3.next = target.next
        target.next = c1
        current = current.next

    current = nodes[0].next
    cups = []
    while current.val != 1:
        cups.append(current.val)
        current = current.next
    return cups


cups = starting_cups
cups = run(cups, 100)
print(''.join(map(str, cups)))

cups = starting_cups + list(range(max(starting_cups) + 1, 10 ** 6 + 1))
cups = run(cups, 10 ** 7)
print(cups[0] * cups[1])
