from lib import load_input
import re


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    res = 0
    for l in data:
        card = l.split(": ")[1]
        winning, ns = card.split(" | ")
        winning = re.split("\\s+", winning.strip())
        ns = re.split("\\s+", ns.strip())
        won = sum((n in winning) for n in ns)
        res += 2 ** (won - 1) if won else 0

    return res


def part_two(data):
    cards = []
    for l in data:
        card = l.split(": ")[1]
        winning, ns = card.split(" | ")
        winning = re.split("\\s+", winning.strip())
        ns = re.split("\\s+", ns.strip())
        cards.append(sum((n in winning) for n in ns))

    ns = [1 for _ in cards]
    for i, n in enumerate(ns):
        for j in range(i + 1, i + cards[i] + 1):
            ns[j] += ns[i]

    return sum(ns)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
