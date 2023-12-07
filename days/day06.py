from lib import load_input
import re
import numpy as np


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    times = [int(n) for n in re.split("\\s+", data[0])[1:]]
    distance = [int(n) for n in re.split("\\s+", data[1])[1:]]

    totals = []
    for i in range(len(times)):
        time = times[i]
        dist = distance[i]
        possibilities = 0
        for j in range(1, time + 1):
            if j * (time - j) > dist:
                possibilities += 1
        totals.append(possibilities)

    return np.prod(totals)


def part_two(data):
    time = int(data[0].split(":")[1].replace(" ", ""))
    dist = int(data[1].split(":")[1].replace(" ", ""))

    start = 0
    end = time
    for j in range(1, time + 1):
        if j * (time - j) > dist:
            start = j
            break

    for j in range(time + 1, 1, -1):
        if j * (time - j) > dist:
            end = j
            break

    return end - start + 1


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
