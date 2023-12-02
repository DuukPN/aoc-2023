from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    colors = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    res = 0
    for line in data:
        game, rounds = line.split(": ")
        idx = int(game.split(" ")[1])

        allowed = True
        for round in rounds.split("; "):
            for color in round.split(", "):
                n, c = color.split(" ")
                allowed &= int(n) <= colors[c]

        if allowed:
            res += idx

    return res


def part_two(data):
    res = 0
    for line in data:
        game, rounds = line.split(": ")

        colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for round in rounds.split("; "):
            for color in round.split(", "):
                n, c = color.split(" ")
                if int(n) > colors[c]:
                    colors[c] = int(n)

        res += colors["red"] * colors["green"] * colors["blue"]

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
