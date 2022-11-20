import heapq
import math
from collections import defaultdict, namedtuple
from dataclasses import dataclass

COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
TARGETS = {"A": 2, "B": 4, "C": 6, "D": 8}
HALL = (0, 1, 3, 5, 7, 9, 10)
PART_TWO = "D#C#B#A\nD#B#A#C".splitlines()

Amphipod = namedtuple("Amphipod", ["symbol", "index", "depth"])


def main():
    with open("input_files/day23", "r") as f:
        lines = f.read().splitlines()[2:-1]
        lines = [line.strip().strip("#").split("#") for line in lines]

    amphipods = frozenset(
        Amphipod(symbol, index * 2, depth)
        for depth, line in enumerate(lines, start=1)
        for index, symbol in enumerate(line, start=1)
    )
    extended_amphipods = frozenset(
        a if a.depth == 1 else Amphipod(a.symbol, a.index, 4) for a in amphipods
    )
    extended_amphipods |= frozenset(
        Amphipod(symbol, index * 2, depth)
        for depth, line in enumerate(PART_TWO, start=2)
        for index, symbol in enumerate(line.split("#"), start=1)
    )
    print(search(State(amphipods, 2)))
    print(search(State(extended_amphipods, 4)))


def search(state):
    h = [(0, state)]
    seen = defaultdict(lambda: math.inf)
    while h:
        cost, state = heapq.heappop(h)
        if len(state.amphipods) == 0:
            return cost
        next_ = state.moves()
        for new_state, added_cost in next_:
            total = added_cost + cost
            if total < seen[new_state]:
                seen[new_state] = total
                heapq.heappush(h, (total, new_state))
    return None


@dataclass(frozen=True, order=True)
class State:
    amphipods: frozenset[Amphipod]
    height: int
    finished: frozenset[Amphipod] = frozenset()

    def path_clear(self, current, destination):
        from_ = min(current + 1, destination)
        to = max(current - 1, destination)
        return not any(
            a.index in range(from_, to + 1) and a.depth == 0
            for a in self.amphipods
        )

    def can_move(self, amphipod):
        return not any(
            a.index == amphipod.index and a.depth < amphipod.depth
            for a in self.amphipods
        )

    def moves_of(self, amphipod):
        amphipods = self.amphipods - {amphipod}
        if amphipod.depth == 0:
            yield from self.move_to_room(amphipod, amphipods)
        elif self.can_move(amphipod):
            yield from self.move_from_room(amphipod, amphipods)

    def move_from_room(self, amphipod, amphipods):
        hallway = {loc for loc in HALL if self.path_clear(amphipod.index, loc)}
        for loc in hallway:
            added_cost = cost_to_move(amphipod, loc)
            new_amphipods = amphipods | {Amphipod(amphipod.symbol, loc, 0)}
            yield State(new_amphipods, self.height, self.finished), added_cost

    def move_to_room(self, amphipod, amphipods):
        target = TARGETS[amphipod.symbol]
        room = {a for a in amphipods | self.finished if a.index == target}
        room_clear = all(a.symbol == amphipod.symbol for a in room)
        if room_clear and self.path_clear(amphipod.index, target):
            new_depth = self.height - len(room)
            added_cost = cost_to_move(amphipod, target, new_depth)
            new_amphipod = Amphipod(amphipod.symbol, target, new_depth)
            new_finished = self.finished | {new_amphipod} | room
            yield State(amphipods - room, self.height, new_finished), added_cost

    def moves(self):
        for amphipod in self.amphipods:
            yield from self.moves_of(amphipod)


def cost_to_move(amphipod, destination, depth=0):
    distance = amphipod.depth + abs(amphipod.index - destination) + depth
    return distance * COST[amphipod.symbol]


if __name__ == "__main__":
    main()
