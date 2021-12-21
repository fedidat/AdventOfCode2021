import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n\n')
    method = [c == '#' for c in data[0].replace('\n', '')]
    grid = data[1].split('\n')
    points = {(j, -1 * i): c == '#' for (i, l) in enumerate(grid) for (j, c) in enumerate(l)}
    return method, points


def do_steps(method, points, steps):
    for step in range(steps):
        next_points = {}
        min_x, max_x = min(pt[0] for pt in points), max(pt[0] for pt in points)
        min_y, max_y = min(pt[1] for pt in points), max(pt[1] for pt in points)
        for row in range(min_x-1, max_x+2):
            for col in range(max_y+1, min_y-2, -1):
                surrounding = ''
                for j in range(col + 1, col - 2, -1):
                    for i in range(row - 1, row + 2):
                        if (i, j) in points:
                            surrounding += '1' if points[(i, j)] else '0'
                        else:
                            surrounding += '1' if method[0] and step % 2 == 1 else '0'
                next_points[(row, col)] = method[int(surrounding, 2)]
        points = next_points
    return points


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        method, points = get_input()
        result = do_steps(method, points, 2)
        print("Part 1:", sum(result.values()))

    def test_star_2(self):
        method, points = get_input()
        result = do_steps(method, points, 50)
        print("Part 2:", sum(result.values()))


if __name__ == '__main__':
    unittest.main()
