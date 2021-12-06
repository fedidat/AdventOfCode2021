import unittest
from collections import defaultdict


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().strip().split(",")]


def solve(data, days):
    count_map = defaultdict(int, {n: data.count(n) for n in set(data)})
    for day in range(0, days):
        for (val, count) in {i: j for (i, j) in count_map.items() if j > 0}.items():
            if val == 0:
                count_map[6] += count
                count_map[8] += count
            else:
                count_map[val - 1] += count
            count_map[val] -= count
    return sum(count_map.values())


class MyTestCase(unittest.TestCase):
    def test_star_1(self):
        print("Part 1:", solve(get_input(), 80))

    def test_star_2(self):
        print("Part 2:", solve(get_input(), 256))


if __name__ == '__main__':
    unittest.main()
