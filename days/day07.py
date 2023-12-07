from lib import load_input
import functools


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    hands = []
    for l in data:
        hand, bid = l.split(" ")
        hands.append((hand, int(bid)))

    hands = sorted(hands, key=lambda x: functools.cmp_to_key(compare_hands)(x[0]))

    res = 0
    for i, (hand, bid) in enumerate(hands):
        res += bid * (i + 1)

    return res


def compare_hands(x, y):
    x_freq = {}
    for i in x:
        if i in x_freq:
            x_freq[i] += 1
        else:
            x_freq[i] = 1

    y_freq = {}
    for i in y:
        if i in y_freq:
            y_freq[i] += 1
        else:
            y_freq[i] = 1

    x_h = max(x_freq, key=lambda x: x_freq[x])
    y_h = max(y_freq, key=lambda y: y_freq[y])

    if x_freq[x_h] > y_freq[y_h]:
        return 1
    elif x_freq[x_h] < y_freq[y_h]:
        return -1
    else:
        x_freq[x_h] = 0
        y_freq[y_h] = 0
        x_h = max(x_freq, key=lambda x: x_freq[x])
        y_h = max(y_freq, key=lambda y: y_freq[y])

        if x_freq[x_h] > y_freq[y_h]:
            return 1
        elif x_freq[x_h] < y_freq[y_h]:
            return -1
        else:
            cards = "AKQJT98765432"
            for i in range(len(x)):
                x_h = cards.index(x[i])
                y_h = cards.index(y[i])
                if x_h > y_h:
                    return -1
                elif x_h < y_h:
                    return 1
            else:
                return 0


def part_two(data):
    hands = []
    for l in data:
        hand, bid = l.split(" ")
        hands.append((hand, int(bid)))

    print(compare_hands2("JKKK2", "QQQQ2"))

    hands = sorted(hands, key=lambda x: functools.cmp_to_key(compare_hands2)(x[0]))

    res = 0
    for i, (hand, bid) in enumerate(hands):
        print(hand, bid)
        res += bid * (i + 1)

    return res


def compare_hands2(x, y):
    x_freq = {}
    for i in x:
        if i in x_freq:
            x_freq[i] += 1
        else:
            x_freq[i] = 1

    y_freq = {}
    for i in y:
        if i in y_freq:
            y_freq[i] += 1
        else:
            y_freq[i] = 1

    x_j = x_freq["J"] if "J" in x_freq else 0
    y_j = y_freq["J"] if "J" in y_freq else 0
    x_freq["J"] = 0
    y_freq["J"] = 0
    x_h = max(x_freq, key=lambda x: x_freq[x])
    y_h = max(y_freq, key=lambda y: y_freq[y])

    if x_freq[x_h] + x_j > y_freq[y_h] + y_j:
        return 1
    elif x_freq[x_h] + x_j < y_freq[y_h] + y_j:
        return -1
    else:
        x_freq[x_h] = 0
        y_freq[y_h] = 0
        x_h = max(x_freq, key=lambda x: x_freq[x])
        y_h = max(y_freq, key=lambda y: y_freq[y])

        if x_freq[x_h] > y_freq[y_h]:
            return 1
        elif x_freq[x_h] < y_freq[y_h]:
            return -1
        else:
            cards = "AKQT98765432J"
            for i in range(len(x)):
                x_h = cards.index(x[i])
                y_h = cards.index(y[i])
                if x_h > y_h:
                    return -1
                elif x_h < y_h:
                    return 1
            else:
                return 0


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
