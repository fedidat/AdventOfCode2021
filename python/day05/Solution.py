import unittest
import re
from collections import defaultdict


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return file.read().strip().split("\n")


def solve_grid(data, allow_diagonal):
    vector = [list(map(int, re.search(r'(\d+),(\d+) -> (\d+),(\d+)', l).groups())) for l in data]
    grid = defaultdict(int)
    for v in vector:
        if v[0] == v[2]:
            for i in range(min(v[1], v[3]), max(v[1], v[3]) + 1):
                grid[(i, v[0])] += 1
        elif v[1] == v[3]:
            for i in range(min(v[0], v[2]), max(v[0], v[2]) + 1):
                grid[(v[1], i)] += 1
        elif allow_diagonal:
            if v[0] - v[2] == v[1] - v[3]:  # both axis advance together
                for i, j in zip(range(min(v[0], v[2]), max(v[0], v[2]) + 1),
                                range(min(v[1], v[3]), max(v[1], v[3]) + 1)):
                    grid[(j, i)] += 1
            else:
                for i, j in zip(range(min(v[0], v[2]), max(v[0], v[2]) + 1),
                                range(max(v[1], v[3]), min(v[1], v[3]) - 1, -1)):
                    grid[(j, i)] += 1
    return grid


class MyTestCase(unittest.TestCase):
    def test_star_1(self):
        data = get_input()
        grid = solve_grid(data, False)
        print("Part 1: " + str(sum(x >= 2 for x in grid.values())))

    def test_star_2(self):
        data = get_input()
        grid = solve_grid(data, True)
        print("Part 2: " + str(sum(x >= 2 for x in grid.values())))


if __name__ == '__main__':
    unittest.main()
