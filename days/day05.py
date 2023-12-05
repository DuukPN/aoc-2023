from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def parse_data(data):
    seeds = [int(n) for n in data[0].split(": ")[1].split(" ")]

    maps = []
    current = None
    for line in data[2:]:
        if line.endswith(":"):
            current = len(maps)
            maps.append([])
        elif line:
            maps[current].append(tuple(int(n) for n in line.split(" ")))

    return seeds, maps


def part_one(data):
    seeds, maps = parse_data(data)

    finals = []
    for seed in seeds:
        curr = seed
        for m in maps:
            for dest_start, src_start, length in m:
                if curr >= src_start and curr < src_start + length:
                    curr = dest_start + (curr - src_start)
                    break
        finals.append(curr)

    return min(finals)


def part_two(data):
    seeds, maps = parse_data(data)

    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for m in maps:
        new_ranges = []
        while seed_ranges:
            (s, l) = seed_ranges.pop(0)
            for dest_start, src_start, length in m:
                if src_start <= s < src_start + length:
                    if s + l <= src_start + length:
                        new_ranges.append((dest_start + s - src_start, l))
                        break
                    else:
                        l1 = (src_start + length) - s
                        new_ranges.append((dest_start + s - src_start, l1))
                        seed_ranges.append((src_start + length, l - l1))
                        break
                elif src_start < s + l <= src_start + length:
                    new_ranges.append((dest_start, s + l - src_start))
                    seed_ranges.append((s, src_start - s))
                    break
            else:
                new_ranges.append((s, l))
        seed_ranges = new_ranges

    return min(r[0] for r in seed_ranges)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
