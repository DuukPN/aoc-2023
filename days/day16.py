from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return simulate(data, ((0, 0), (0, 1)))


def simulate(data, beam):
    energized = [[set() for _ in line] for line in data]
    beams = [beam]
    while beams:
        new_beams = []
        for (x, y), (dx, dy) in beams:
            if not 0 <= x < len(energized) or not 0 <= y < len(energized[0]) or (dx, dy) in energized[x][y]:
                continue
            energized[x][y].add((dx, dy))
            if data[x][y] == "|":
                if dy:
                    new_beams.append(((x + 1, y), (1, 0)))
                    new_beams.append(((x - 1, y), (-1, 0)))
                else:
                    new_beams.append(((x + dx, y + dy), (dx, dy)))
            elif data[x][y] == "-":
                if dx:
                    new_beams.append(((x, y + 1), (0, 1)))
                    new_beams.append(((x, y - 1), (0, -1)))
                else:
                    new_beams.append(((x + dx, y + dy), (dx, dy)))
            elif data[x][y] == "\\":
                new_beams.append(((x + dy, y + dx), (dy, dx)))
            elif data[x][y] == "/":
                new_beams.append(((x - dy, y - dx), (-dy, -dx)))
            else:
                new_beams.append(((x + dx, y + dy), (dx, dy)))

        beams = new_beams

    res = sum(sum(bool(c) for c in line) for line in energized)
    return res


def part_two(data):
    beams = []
    for x in range(len(data)):
        beams.append(((x, 0), (0, 1)))
        beams.append(((x, len(data[x]) - 1), (0, -1)))

    for y in range(len(data[0])):
        beams.append(((0, y), (1, 0)))
        beams.append(((len(data) - 1, y), (-1, 0)))

    return max(simulate(data, beam) for beam in beams)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
