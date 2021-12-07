import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().strip().split(",")]


def solve(data, distance_function):
    min_dst = float('inf')
    for dst in range(min(data), max(data) + 1):
        cost = 0
        for pt in data:
            cost += distance_function(pt, dst)
        min_dst = min(min_dst, cost)
    return min_dst


class MyTestCase(unittest.TestCase):
    def test_star_1(self):
        data = get_input()
        print("Part 1:", solve(data, lambda src, dst: abs(dst - src)))
        # or median: data.sort() then sum(abs(pt - data[len(data) // 2]) for pt in data)

    def test_star_2(self):
        data = get_input()
        print("Part 2:", solve(data, lambda src, dst: abs(dst - src) * (abs(dst - src) + 1) // 2))


if __name__ == '__main__':
    unittest.main()
