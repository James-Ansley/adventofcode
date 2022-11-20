from z3 import If, Int, Optimize

# Generate CSV
# with open("input_files/day24", "r") as f:
#     instructions = f.read().strip("inp w\n").split("inp w\n")
#     instructions = [e.splitlines() for e in instructions]
#     instructions = [*zip(*zip(*instructions))]
#     print("\n".join(",".join(("inp w", *line)) for line in instructions))

A = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]
B = [12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12]
C = [6, 2, 13, 8, 13, 8, 3, 11, 10, 8, 14, 6, 8, 2]


def solve(a, b, c, maximise):
    # Huge thank you to fuglede for their solution on this one
    # https://github.com/fuglede
    # Fingers crossed there isn't another question like this next year!
    solver = Optimize()
    w = [Int(f"w{i}") for i in range(14)]
    for wi in w:
        solver.add(0 < wi, wi <= 9)
        if maximise:
            solver.maximize(wi)
        else:
            solver.minimize(wi)

    z = 0
    for wi, ai, bi, ci in zip(w, a, b, c):
        z = If(
            z % 26 + bi != wi,
            z / ai * 26 + wi + ci,
            z / ai,
        )
    solver.add(z == 0)
    solver.check()
    return "".join(solver.model()[wi].as_string() for wi in w)


print(solve(A, B, C, True))
print(solve(A, B, C, False))
