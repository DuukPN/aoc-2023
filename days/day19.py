from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    workflows = {}
    parts = []
    switch = False
    for line in data:
        if not line:
            switch = True
            continue

        if not switch:
            label, rules = line[:-1].split("{")
            workflows[label] = []
            for rule in rules.split(","):
                workflows[label].append(tuple(rule.split(":")))
        else:
            parts.append(tuple([int(a.split("=")[1]) for a in line[1:-1].split(",")]))

    res = 0
    for x, m, a, s in parts:
        curr = "in"
        while curr != "A" and curr != "R":
            workflow = workflows[curr]
            for rule in workflow:
                if len(rule) == 2:
                    if eval(rule[0]):
                        curr = rule[1]
                        break
                else:
                    curr = rule[0]

        if curr == "A":
            res += x + m + a + s

    return res


def part_two(data):
    workflows = {}
    for line in data:
        if not line:
            break

        label, rules = line[:-1].split("{")
        workflows[label] = []
        for rule in rules.split(","):
            workflows[label].append(tuple(rule.split(":")))

    accepting = find_accepting(workflows, "in", 0)

    res = 0
    for path in accepting:
        vars = {
            "x": [1, 4000],
            "m": [1, 4000],
            "a": [1, 4000],
            "s": [1, 4000]
        }
        for rule in path:
            n = int(rule[3:])
            var = vars[rule[0]]
            if rule[1:3] == ">>":
                var[0] = max(var[0], n + 1)
            elif rule[1:3] == ">=":
                var[0] = max(var[0], n)
            elif rule[1:3] == "<<":
                var[1] = min(var[1], n - 1)
            elif rule[1:3] == "<=":
                var[1] = min(var[1], n)

        tot = 1
        for a, b in vars.values():
            tot *= b - a + 1
        res += tot
    return res


def find_accepting(workflows, curr, i):
    if curr == "A":
        return [[]]
    elif curr == "R":
        return []
    rule = workflows[curr][i]
    if len(rule) == 1:
        return find_accepting(workflows, rule[0], 0)

    left = find_accepting(workflows, rule[1], 0)
    right = find_accepting(workflows, curr, i + 1)
    l = [[rule[0].replace("<", "<<").replace(">", ">>")] + a for a in left]
    r = [[flip_sign(rule[0])] + a for a in right]
    return l + r


def flip_sign(rule):
    if ">" in rule:
        return rule.replace(">", "<=")
    else:
        return rule.replace("<", ">=")


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
