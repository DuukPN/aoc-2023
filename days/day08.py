import numpy as np

from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    instrs = data[0]
    nodes = {}
    for line in data[2:]:
        name, adj = line[:-1].split(" = (")
        nodes[name] = tuple(adj.split(", "))

    i = 0
    curr = "AAA"
    while True:
        d = instrs[i % len(instrs)]
        i += 1

        curr = nodes[curr][0 if d == "L" else 1]

        if curr == "ZZZ":
            return i


def part_two(data):
    instrs = data[0]
    nodes = {}
    for line in data[2:]:
        name, adj = line[:-1].split(" = (")
        nodes[name] = tuple(adj.split(", "))

    init = [n for n in nodes.keys() if n.endswith("A")]
    cycles = []

    for curr in init:
        cycle = []
        i = 0
        n = len(instrs)
        while True:
            d = instrs[i % len(instrs)]
            i += 1

            curr = nodes[curr][0 if d == "L" else 1]

            if curr.endswith("Z"):
                if cycle:
                    first, idx = cycle[0]
                    if (curr, i % n) == (first, idx % n):
                        cycle.append((curr, i))
                        cycles.append(cycle)
                        break
                cycle.append((curr, i))

    cycles = list(map(lambda x: x[0][1], cycles))
    lcm = 1
    for c in cycles:
        lcm = np.lcm(c, lcm, dtype=object)

    return lcm


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
