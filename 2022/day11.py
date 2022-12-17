import heapq
import re
from collections import deque
from math import prod
from operator import add, mul

pattern = r"""Monkey (?P<id>\d+):
  Starting items: (?P<items>.+)
  Operation: new = (?P<op>.+)
  Test: divisible by (?P<cond>\d+)
    If true: throw to monkey (?P<if_true>\d+)
    If false: throw to monkey (?P<if_false>\d+)"""

with open("input_files/day11", "r") as f:
    data = re.finditer(pattern, f.read())
    data = [m.groupdict() for m in data]

ops = {"*": mul, "+": add}
monkeys = {}
for monkey in data:
    match monkey["op"].split():
        case ["old", op, "old"]:
            operation = lambda x, op=ops[op]: op(x, x)
        case ["old", op, v]:
            operation = lambda x, op=ops[op], v=v: op(x, int(v))
    monkeys[monkey["id"]] = {
        "items": [int(item) for item in monkey["items"].split(", ")],
        "op": operation,
        "cond": int(monkey["cond"]),
        "if_true": monkey["if_true"],
        "if_false": monkey["if_false"],
    }


def run(rounds, worry_factor):
    data = {id_: {"items": deque(m["items"]), "inspected": 0}
            for id_, m in monkeys.items()}
    mod_by = prod(m["cond"] for m in monkeys.values())
    for _ in range(rounds):
        for m_id, monkey in monkeys.items():
            m_data = data[m_id]
            while m_data["items"]:
                item = m_data["items"].popleft()
                item = (monkey["op"](item) // worry_factor) % mod_by
                m_data["inspected"] += 1
                if item % monkey["cond"] == 0:
                    next_monkey = monkey["if_true"]
                else:
                    next_monkey = monkey["if_false"]
                data[next_monkey]["items"].append(item)
    m1, m2 = heapq.nlargest(2, [m["inspected"] for m in data.values()])
    return m1 * m2


print(run(20, 3))
print(run(10000, 1))
