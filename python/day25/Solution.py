import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')


def solve(grid):
    for i in range(1, 1000):
        grid1 = [s for s in grid]
        for y, line in enumerate(grid):
            for x, c in enumerate(line):
                if c == '>' and line[(x+1) % len(line)] == '.':
                    s = list(grid1[y])
                    s[x] = '.'
                    s[(x+1) % len(line)] = '>'
                    grid1[y] = ''.join(s)
        grid2 = [s for s in grid1]
        for y, line in enumerate(grid1):
            for x, c in enumerate(line):
                if c == 'v' and grid1[(y+1) % len(grid1)][x] == '.':
                    grid2[y] = grid2[y][:x] + '.' + grid2[y][x+1:]
                    grid2[(y+1) % len(grid1)] = grid2[(y+1) % len(grid1)][:x] + 'v' + grid2[(y+1) % len(grid1)][x+1:]
        if grid == grid2:
            return i
        grid = grid2
    return float('inf')


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        print("Part 1:", solve(data))


if __name__ == '__main__':
    unittest.main()
