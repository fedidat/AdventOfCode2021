import unittest


def get_input():
    filename = "input"
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')


def solve(instr, inc):
    stack = []
    val = 11111111111111 if inc else 99999999999999
    for i in range(14):
        x = int(instr[18*i+5].split(" ")[-1])
        y = int(instr[18*i+15].split(" ")[-1])
        if x > 0:
            stack += [(i, y)]
            continue
        j, y = stack.pop()
        val = val + (1 if inc else -1) * abs((x + y) * 10 ** (13 - [i, j][(x < -y if inc else x > -y)]))
    return val


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        print("Part 1:", solve(data, False))

    def test_star_2(self):
        data = get_input()
        print("Part 2:", solve(data, True))


if __name__ == '__main__':
    unittest.main()
