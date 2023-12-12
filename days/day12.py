import re

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
        springs, groups = line.split(" ")
        groups = [int(n) for n in groups.split(",")]

        res += solve_line(springs, groups)

    return res


def part_two(data):
    res = 0
    for line in data:
        springs1, groups = line.split(" ")
        groups = [int(n) for n in groups.split(",")] * 5
        springs = springs1
        for _ in range(4):
            springs = springs + "?" + springs1

        res += solve_line(springs, groups)

    return res


def solve_line(springs, groups):
    arr = [[0 for _ in springs] for _ in groups]

    for k, group in enumerate(groups):
        if k == 0:
            for i in range(len(arr[0])):
                arr[0][i] = int(
                    check_damaged(springs, i - group + 1, group) and check_operational(springs, 0, i - group + 1))
            continue

        for i in range(len(arr[k])):
            for j in range(i - group):
                if (check_damaged(springs, i - group + 1, group)
                        and check_operational(springs, j + 1, i - j - group)):
                    arr[k][i] += arr[k - 1][j]

    res = 0
    for i in range(len(arr[-1])):
        if arr[-1][i] and check_operational(springs, i + 1, len(arr[-1]) - i - 1):
            res += arr[-1][i]

    return res


def check_damaged(springs, i, group):
    if i < 0 or i + group > len(springs):
        return False

    return bool(re.match("^[?#]*$", springs[i:i+group]))


def check_operational(springs, i, space):
    if i < 0 or i + space > len(springs):
        return False

    return bool(re.match("^[?.]*$", springs[i:i+space]))


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
