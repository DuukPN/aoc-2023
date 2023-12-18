from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    trenches = []
    dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    for line in data:
        d, n, color = line.split(" ")
        trenches.append((dirs[d], int(n)))

    return solve_grid(trenches)


def part_one_first(data):
    trenches = []
    right = 1
    down = 1
    left = 1
    up = 1
    start_x = 0
    start_y = 0
    dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    for line in data:
        d, n, color = line.split(" ")
        trenches.append((dirs[d], int(n), color))
        if d == "R":
            right += int(n)
        elif d == "D":
            down += int(n)
        elif d == "U":
            up += int(n)
        elif d == "L":
            left += int(n)
        start_y = max(start_y, left - right)
        start_x = max(start_x, up - down)

    grid = [["." for _ in range(right + start_y)] for _ in range(start_x, down)]
    x, y = start_x, start_y
    grid[x][y] = "c"
    for (dx, dy), n, _ in trenches:
        for _ in range(n):
            x += dx
            y += dy
            grid[x][y] = "|" if dx else "-"
        grid[x][y] = "c"

    inside = False
    res = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "|":
                res += 1
                inside ^= True
            elif c == "-":
                res += 1
            elif c == "c":
                res += 1
                if i > 0 and (grid[i-1][j] == "|" or grid[i-1][j] == "c"):
                    inside ^= True
            elif inside:
                res += 1

    return res


def solve_grid(trenches):
    corners = []
    px, py = trenches[-1][0]
    x, y = 0, 0
    for (dx, dy), n in trenches:
        corners.append((x + (py + dy == -1), y + (px + dx == 1)))
        x += dx * n
        y += dy * n
        px, py = dx, dy

    res = 0
    for i in range(len(corners)):
        x1, y1 = corners[i - 1]
        x2, y2 = corners[i]
        res += x1 * y2 - x2 * y1

    return res // -2


def part_two(data):
    trenches = []
    dirs = {"0": (0, 1), "2": (0, -1), "3": (-1, 0), "1": (1, 0)}
    for line in data:
        d, n, color = line.split(" ")
        trenches.append((dirs[color[-2]], int(color[2:-2], 16)))

    return solve_grid(trenches)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
