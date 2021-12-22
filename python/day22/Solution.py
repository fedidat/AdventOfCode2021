from collections import defaultdict
import unittest
import re


def get_input():
    # filename = "sample"
    # filename = "sample2"
    filename = "input"
    with open(filename, 'r') as file:
        return [(1 if line.startswith("on") else -1, [int(s) for s in re.findall(r'-?\d+', line)])
                for line in file.read().strip().split('\n')]


def run_sequence(data):
    cubes = defaultdict(int)
    for sign, (x0, x1, y0, y1, z0, z1) in data:  # for each new cuboid
        update = defaultdict(int)
        for (_x0, _x1, _y0, _y1, _z0, _z1), _sign in cubes.items():  # for each existing including intersections
            ix0, ix1 = max(x0, _x0), min(x1, _x1)
            iy0, iy1 = max(y0, _y0), min(y1, _y1)
            iz0, iz1 = max(z0, _z0), min(z1, _z1)
            if ix1-ix0 >= 0 and iy1-iy0 >= 0 and iz1-iz0 >= 0:
                update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= _sign  # remove intersections with new cube
        if sign > 0:
            update[(x0, x1, y0, y1, z0, z1)] += sign  # if switching on, add to cubes
        cubes.update(update)
    return cubes


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        filtered_data = [line for line in data if all(-50 < val < 50 for val in line[1])]
        cubes = run_sequence(filtered_data)
        on_cubes = sum(sign * (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)
                       for (x0, x1, y0, y1, z0, z1), sign in cubes.items())
        print("Part 1:", on_cubes)

    def test_star_2(self):
        data = get_input()
        cubes = run_sequence(data)
        on_cubes = sum(sign * (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)
                       for (x0, x1, y0, y1, z0, z1), sign in cubes.items())
        print("Part 2:", on_cubes)


if __name__ == '__main__':
    unittest.main()
