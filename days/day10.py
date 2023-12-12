from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    start = None
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dirmap = {
        ("-", (0, 1)): (0, 1),
        ("-", (0, -1)): (0, -1),
        ("|", (1, 0)): (1, 0),
        ("|", (-1, 0)): (-1, 0),
        ("7", (0, 1)): (1, 0),
        ("7", (-1, 0)): (0, -1),
        ("J", (1, 0)): (0, -1),
        ("J", (0, 1)): (-1, 0),
        ("L", (0, -1)): (-1, 0),
        ("L", (1, 0)): (0, 1),
        ("F", (-1, 0)): (0, 1),
        ("F", (0, -1)): (1, 0)
    }
    connect = {
        (-1, 0): {"|", "7", "F"},
        (0, 1): {"-", "7", "J"},
        (1, 0): {"|", "L", "J"},
        (0, -1): {"-", "L", "F"}
    }
    adj = []
    prevs = []
    for (di, dj) in dirs:
        i, j = start
        if (i + di in range(len(data))
                and j + dj in range(len(data[0]))
                and data[i + di][j + dj] in connect[(di, dj)]):
            adj.append((i + di, j + dj))
            prevs.append((di, dj))

    curr1, curr2 = adj
    prev1, prev2 = prevs
    res = 1
    while curr1 != curr2:
        res += 1
        i, j = curr1
        (di, dj) = dirmap[(data[i][j], prev1)]
        curr1 = (i + di, j + dj)
        prev1 = (di, dj)

        i, j = curr2
        (di, dj) = dirmap[(data[i][j], prev2)]
        curr2 = (i + di, j + dj)
        prev2 = (di, dj)

    return res


def part_two(data):
    start = None
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    all_chars = {"|", "-", "7", "J", "F", "L"}
    dirmap = {
        ("-", (0, 1)): (0, 1),
        ("-", (0, -1)): (0, -1),
        ("|", (1, 0)): (1, 0),
        ("|", (-1, 0)): (-1, 0),
        ("7", (0, 1)): (1, 0),
        ("7", (-1, 0)): (0, -1),
        ("J", (1, 0)): (0, -1),
        ("J", (0, 1)): (-1, 0),
        ("L", (0, -1)): (-1, 0),
        ("L", (1, 0)): (0, 1),
        ("F", (-1, 0)): (0, 1),
        ("F", (0, -1)): (1, 0)
    }
    connect = {
        (-1, 0): {"|", "7", "F"},
        (0, 1): {"-", "7", "J"},
        (1, 0): {"|", "L", "J"},
        (0, -1): {"-", "L", "F"}
    }
    adj = []
    prevs = []
    for (di, dj) in dirs:
        i, j = start
        if (i + di in range(len(data))
                and j + dj in range(len(data[0]))
                and data[i + di][j + dj] in connect[(di, dj)]):
            adj.append((i + di, j + dj))
            prevs.append((di, dj))

    curr1, curr2 = adj
    prev1, prev2 = prevs
    char, = all_chars.difference(connect[prev1].union(connect[prev2]))
    data[i] = data[i][:j] + char + data[i][j + 1:]
    loop = [set() for _ in data]
    loop[start[0]].add(start[1])
    while curr1 != curr2:
        i, j = curr1
        loop[i].add(j)
        (di, dj) = dirmap[(data[i][j], prev1)]
        curr1 = (i + di, j + dj)
        prev1 = (di, dj)

        i, j = curr2
        loop[i].add(j)
        (di, dj) = dirmap[(data[i][j], prev2)]
        curr2 = (i + di, j + dj)
        prev2 = (di, dj)

    loop[curr1[0]].add(curr1[1])

    res = 0
    for i, line in enumerate(data):
        consts = loop[i]
        count = False
        start = None
        for j, c in enumerate(line):
            if j in consts:
                if c not in connect[(0, 1)]:
                    count ^= True
                    if c != "|":
                        start = dirmap[(c, (0, -1))]
                else:
                    if start == dirmap[(c, (0, 1))]:
                        count ^= True
            else:
                if count:
                    res += 1

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
