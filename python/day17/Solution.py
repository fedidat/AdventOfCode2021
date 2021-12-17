import re
import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        data = file.read().strip()
        m = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data)
        return [int(s) for s in m.groups()]


def simulate(x0, x1, y0, y1, x, y, vx, vy):
    if x > x1 or y < y0:
        return False
    if x >= x0 and y <= y1:
        return True
    return simulate(x0, x1, y0, y1, x + vx, y + vy, vx - (vx > 0), vy - 1)


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        # we want to reach the target with vx = 0 for max steps, allowing for larger y
        # thus, by the time we reach vx = 0, we also have vy = -vy_start
        # meaning, vy = -y0 - 1, and summing up the series y_top = y0 * (y0 + 1)
        _, _, y0, _ = get_input()
        print("Part 1:", y0 * (y0 + 1) // 2)

    def test_star_2(self):
        x0, x1, y0, y1 = get_input()
        hits = [simulate(x0, x1, y0, y1, 0, 0, x, y) for x in range(1, 1 + x1) for y in range(y0, -y0)]
        print("Part 2:", sum(hits))


if __name__ == '__main__':
    unittest.main()
