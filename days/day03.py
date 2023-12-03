from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one_attempt(lines)
    elif part == 2:
        return part_two(lines)


idx = 0

def replace_numbers(line: str):
    l = [c for c in line]
    n = ""
    global idx
    for i, c in enumerate(l):
        if c.isdigit():
            n += c
        else:
            j = i - 1
            while j >= 0 and l[j].isdigit():
                l[j] = (idx, int(n))
                j -= 1
            idx += 1
            n = ""
    return l


def part_one(data):
    res = 0
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if not c.isdigit() and c != '.':
                searched = set()
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if (di, dj) not in searched:
                        if data[i + di][j + dj].isdigit():
                            x = dj - 1
                            while j + x in range(len(line)) and data[i + di][j + x].isdigit():
                                searched.add((di, x))
                                x -= 1
                            x += 1
                            n = ""
                            while j + x in range(len(line)) and data[i + di][j + x].isdigit():
                                n += data[i + di][j + x]
                                searched.add((di, x))
                                x += 1
                            res += int(n)
                        searched.add((di, dj))

    print(res)


def part_one_attempt(data):
    data = [replace_numbers(line) for line in data]
    res = 0
    added = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if isinstance(c, str) and c != '.':
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if i + di in range(len(data)) and j + dj in range(len(line)):
                        n = data[i + di][j + dj]
                        if isinstance(n, tuple) and n[0] not in added:
                            print(n)
                            res += n[1]
                            added.add(n[0])

    return res


def part_two(data):
    res = 0
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '*':
                ns = []
                searched = set()
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if (di, dj) not in searched:
                        if data[i + di][j + dj].isdigit():
                            x = dj - 1
                            while j + x in range(len(line)) and data[i + di][j + x].isdigit():
                                searched.add((di, x))
                                x -= 1
                            x += 1
                            n = ""
                            while j + x in range(len(line)) and data[i + di][j + x].isdigit():
                                n += data[i + di][j + x]
                                searched.add((di, x))
                                x += 1
                            ns.append(int(n))
                        searched.add((di, dj))
                if len(ns) == 2:
                    res += ns[0] * ns[1]

    print(res)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
