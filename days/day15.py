from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    res = 0
    for word in data[0].split(","):
        res += hash_word(word)

    return res


def hash_word(word):
    cur = 0
    for c in word:
        cur += ord(c)
        cur *= 17
        cur = cur % 256

    return cur


def part_two(data):
    boxes = [[] for _ in range(256)]
    for word in data[0].split(","):
        if "=" in word:
            label, length = word.split("=")
            h = hash_word(label)
            for i, (l, v) in enumerate(boxes[h]):
                if l == label:
                    boxes[h][i] = (label, int(length))
                    break
            else:
                boxes[h].append((label, int(length)))
        else:
            h = hash_word(word[:-1])
            for l, v in boxes[h]:
                if l == word[:-1]:
                    boxes[h].remove((l, v))
                    break

    res = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            res += (i + 1) * (j + 1) * lens[1]

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
