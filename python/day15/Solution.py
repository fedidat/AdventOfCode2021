import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return [[int(c) for c in s] for s in file.read().strip().split("\n")]


def dijkstra(grid, src, dst):
    shortest_paths = {}
    queue = [(0, src[0], src[1])]
    while queue:
        queue = [(steps, x, y) for steps, x, y in queue
                 if (x, y) not in shortest_paths or shortest_paths[(x, y)] > steps]
        path, x, y = min(queue)
        queue.remove((path, x, y))
        shortest_paths[(x, y)] = path
        if (x, y) == dst:
            return shortest_paths[(x, y)]
        for (ox, oy) in [(x, y+1), (x-1, y), (x+1, y), (x, y-1)]:
            if (ox, oy) in grid:
                queue.append((path + grid[(ox, oy)], ox, oy))


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        grid = {(x, y): data[y][x] for x in range(len(data[0])) for y in range(len(data))}
        print("Part 1:", dijkstra(grid, (0, 0), (len(data[0]) - 1, len(data) - 1)))

    def test_star_2(self):
        data = get_input()
        grid = {(x, y): data[y][x] for x in range(len(data[0])) for y in range(len(data))}

        x_extensions = {}
        for x, y in grid:
            for i in range(1, 5):
                x_extensions[(x + i * len(data[0]), y)] = (grid[(x, y)] + i - 1) % 9 + 1
        grid.update(x_extensions)

        y_extensions = {}
        for x, y in grid:
            for i in range(1, 5):
                y_extensions[(x, y + i * len(data))] = (grid[(x, y)] + i - 1) % 9 + 1
        grid.update(y_extensions)

        print("Part 2:", dijkstra(grid, (0, 0), (len(data[0]) * 5 - 1, len(data) * 5 - 1)))


if __name__ == '__main__':
    unittest.main()
