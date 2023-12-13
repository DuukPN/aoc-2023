from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def parse_grids(data):
    grids = [[]]
    for line in data:
        if line:
            grids[-1].append(line)
        else:
            grids.append([])

    return grids


def part_one(data):
    grids = parse_grids(data)
    res = 0
    for grid in grids:
        for i in range(1, len(grid)):
            if grid[i] == grid[i - 1] and check_mirror_horizontal(grid, i, 0):
                res += 100 * i
                break
        else:
            for i in range(1, len(grid[0])):
                if [line[i] for line in grid] == [line[i - 1] for line in grid] and check_mirror_vertical(grid, i, 0):
                    res += i

    return res


def check_mirror_horizontal(grid, i, smudge):
    j = i - 1
    while j >= 0 and i < len(grid):
        e = row_diff(grid[i], grid[j])
        if e > smudge:
            return False
        smudge -= e
        i += 1
        j -= 1

    return smudge == 0


def check_mirror_vertical(grid, i, smudge):
    j = i - 1
    while j >= 0 and i < len(grid[0]):
        e = row_diff([line[i] for line in grid], [line[j] for line in grid])
        if e > smudge:
            return False
        smudge -= e
        i += 1
        j -= 1

    return smudge == 0


def part_two(data):
    grids = parse_grids(data)
    res = 0
    for grid in grids:
        for i in range(1, len(grid)):
            e = row_diff(grid[i], grid[i - 1])
            if e < 2 and check_mirror_horizontal(grid, i, 1):
                res += 100 * i
                break
        else:
            for i in range(1, len(grid[0])):
                e = row_diff([line[i] for line in grid], [line[i - 1] for line in grid])
                if e < 2 and check_mirror_vertical(grid, i, 1):
                    res += i

    return res


def row_diff(a, b):
    if len(a) != len(b):
        return -1

    diff = 0
    for i in range(len(a)):
        diff += (a[i] != b[i])

    return diff


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
