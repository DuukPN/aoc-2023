from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    res = 0
    for l in data:
        n = ""
        for c in l:
            if c.isdigit():
                n += c
                break

        for c in reversed(l):
            if c.isdigit():
                n += c
                break

        res += int(n)

    return res


def part_two(data):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    res = 0
    for l in data:
        n = ""
        for c in (range(len(l))):
            if l[c].isdigit():
                n += l[c]
                break
            arr = [l[c:].startswith(d) for d in digits]
            if any(arr):
                n += str(arr.index(True))
                break

        for c in reversed(range(len(l))):
            if l[c].isdigit():
                n += l[c]
                break
            arr = [l[:c+1].endswith(d) for d in digits]
            if any(arr):
                n += str(arr.index(True))
                break

        res += int(n)

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
