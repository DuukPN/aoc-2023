from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    xs = set()
    ys = set()
    galaxies = []
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "#":
                xs.add(i)
                ys.add(j)
                galaxies.append((i, j))

    xs = set(range(len(data))).difference(xs)
    ys = set(range(len(data[0]))).difference(ys)

    res = 0
    for (ai, aj), (bi, bj) in [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]:
        xrange = range(min(ai, bi), max(ai, bi))
        dx = len(xrange) + len(set(xrange).intersection(xs))

        yrange = range(min(aj, bj), max(aj, bj))
        dy = len(yrange) + len(set(yrange).intersection(ys))

        res += dx + dy

    return res


def part_two(data):
    xs = set()
    ys = set()
    galaxies = []
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "#":
                xs.add(i)
                ys.add(j)
                galaxies.append((i, j))

    xs = set(range(len(data))).difference(xs)
    ys = set(range(len(data[0]))).difference(ys)

    res = 0
    for (ai, aj), (bi, bj) in [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]:
        xrange = range(min(ai, bi), max(ai, bi))
        dx = len(xrange) + 999999 * len(set(xrange).intersection(xs))

        yrange = range(min(aj, bj), max(aj, bj))
        dy = len(yrange) + 999999 * len(set(yrange).intersection(ys))

        res += dx + dy

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
