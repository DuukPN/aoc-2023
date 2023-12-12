from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    res = 0
    for line in data:
        vs = [int(n) for n in line.split(" ")]
        hist = [vs]
        while any(vs):
            vs = [vs[i] - vs[i-1] for i in range(1, len(vs))]
            hist.append(vs)

        for i in reversed(range(len(hist))):
            if not any(hist[i]):
                hist[i].append(0)
            else:
                hist[i].append(hist[i][-1] + hist[i+1][-1])

        res += hist[0][-1]

    return res


def part_two(data):
    res = 0
    for line in data:
        vs = [int(n) for n in line.split(" ")]
        hist = [vs]
        while any(vs):
            vs = [vs[i] - vs[i - 1] for i in range(1, len(vs))]
            hist.append(vs)

        for i in reversed(range(len(hist))):
            if not any(hist[i]):
                hist[i].insert(0, 0)
            else:
                hist[i].insert(0, hist[i][0] - hist[i + 1][0])

        res += hist[0][0]

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
