from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    arr = [[c for c in line] for line in data]
    res = 0
    for i, line in enumerate(arr):
        for j, c in enumerate(line):
            if c == "O":
                k = i - 1
                while k >= 0 and arr[k][j] == ".":
                    arr[k][j] = "O"
                    arr[k + 1][j] = "."
                    k -= 1
                res += len(arr) - k - 1

    return res


def part_two(data):
    old_arrs = [] # [[c for c in line] for line in data]
    arr = [[c for c in line] for line in data]

    while arr not in old_arrs:
        old_arrs.append([[c for c in line] for line in arr])

        for i, line in enumerate(arr):
            for j, c in enumerate(line):
                if c == "O":
                    k = i - 1
                    while k >= 0 and arr[k][j] == ".":
                        arr[k][j] = "O"
                        arr[k + 1][j] = "."
                        k -= 1

        for i, line in enumerate(arr):
            for j, c in enumerate(line):
                if c == "O":
                    k = j - 1
                    while k >= 0 and arr[i][k] == ".":
                        arr[i][k] = "O"
                        arr[i][k + 1] = "."
                        k -= 1

        for i, line in reversed(list(enumerate(arr))):
            for j, c in reversed(list(enumerate(line))):
                if c == "O":
                    k = i + 1
                    while k < len(arr) and arr[k][j] == ".":
                        arr[k][j] = "O"
                        arr[k - 1][j] = "."
                        k += 1

        for i, line in reversed(list(enumerate(arr))):
            for j, c in reversed(list(enumerate(line))):
                if c == "O":
                    k = j + 1
                    while k < len(arr) and arr[i][k] == ".":
                        arr[i][k] = "O"
                        arr[i][k - 1] = "."
                        k += 1

    rounds = 1000000000
    first = old_arrs.index(arr)
    cycle = len(old_arrs) - first
    idx = (rounds - first) % cycle + first
    arr = old_arrs[idx]

    res = 0
    for i, line in enumerate(arr):
        for j, c in enumerate(line):
            if c == "O":
                res += len(arr) - i

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
