import unittest
import itertools
from collections import Counter


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    scanners = []
    cur = None
    for line in lines:
        if line == "":
            continue
        elif line[0:3] == "---":
            cur = []
            scanners.append(cur)
        else:
            cur.append(tuple(map(int, line.split(","))))
    return scanners


def try_align(aligned, candidate):
    ret = []
    dl = []
    dp = dpp = None
    for dim in range(3):
        x = [pos[dim] for pos in aligned]
        for (d, s) in [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]:
            if d == dp or d == dpp:
                continue
            t = [pos[d] * s for pos in candidate]
            w = [b - a for (a, b) in itertools.product(x, t)]
            c = Counter(w).most_common(1)
            if c[0][1] >= 12:
                break
        if c[0][1] < 12:
            return None
        (dpp, dp) = (dp, d)
        ret.append([v - c[0][0] for v in t])
        dl.append(c[0][0])
    return list(zip(ret[0], ret[1], ret[2])), dl


def solve(scanners):
    beacons = set()
    next_scanners = [scanners[0]]
    rest = scanners[1:]
    shifts = [(0, 0, 0)]
    while next_scanners:
        aligned = next_scanners.pop()
        tmp = []
        for candidate in rest:
            r = try_align(aligned, candidate)
            if r:
                (updated, shift) = r
                shifts.append(shift)
                next_scanners.append(updated)
            else:
                tmp.append(candidate)
        rest = tmp
        beacons.update(aligned)
    return beacons, shifts


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        done, _ = solve(data)
        print("Part 1:", len(done))

    def test_star_2(self):
        data = get_input()
        _, shifts = solve(data)
        max_distance = 0
        for left in shifts:
            for right in shifts:
                max_distance = max(max_distance, sum(abs(a - b) for (a, b) in zip(left, right)))
        print("Part 2:", max_distance)


if __name__ == '__main__':
    unittest.main()
