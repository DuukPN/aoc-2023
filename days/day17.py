from queue import PriorityQueue

from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    data = [[int(n) for n in line] for line in data]
    visited = [[set() for _ in line] for line in data]
    pq = PriorityQueue()
    pq.put((0, (0, 0, 0, 1)))
    pq.put((0, (0, 0, 1, 0)))

    while not pq.empty():
        dist, (x, y, dx, dy) = pq.get()
        loss = 0
        if (x, y) == (len(data) - 1, len(data[0]) - 1):
            return dist
        if (dx, dy) in visited[x][y]:
            continue
        visited[x][y].add((dx, dy))
        for n in range(1, 4):
            if not (0 <= x + n * dx < len(data) and 0 <= y + n * dy < len(data[0])):
                break
            loss += data[x + n * dx][y + n * dy]
            if (dy, dx) not in (visited[x + n * dx][y + n * dy]):
                pq.put((dist + loss, (x + n * dx, y + n * dy, dy, dx)))
            if (-dy, -dx) not in (visited[x + n * dx][y + n * dy]):
                pq.put((dist + loss, (x + n * dx, y + n * dy, -dy, -dx)))


def part_two(data):
    data = [[int(n) for n in line] for line in data]
    visited = [[set() for _ in line] for line in data]
    pq = PriorityQueue()
    pq.put((0, (0, 0, 0, 1)))
    pq.put((0, (0, 0, 1, 0)))

    while not pq.empty():
        dist, (x, y, dx, dy) = pq.get()
        loss = 0
        if (x, y) == (len(data) - 1, len(data[0]) - 1):
            return dist
        if (dx, dy) in visited[x][y]:
            continue
        visited[x][y].add((dx, dy))
        for n in range(1, 11):
            if not (0 <= x + n * dx < len(data) and 0 <= y + n * dy < len(data[0])):
                break
            loss += data[x + n * dx][y + n * dy]
            if n >= 4:
                if (dy, dx) not in (visited[x + n * dx][y + n * dy]):
                    pq.put((dist + loss, (x + n * dx, y + n * dy, dy, dx)))
                if (-dy, -dx) not in (visited[x + n * dx][y + n * dy]):
                    pq.put((dist + loss, (x + n * dx, y + n * dy, -dy, -dx)))


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
