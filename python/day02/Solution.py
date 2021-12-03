import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return [s.split(" ") for s in file.read().split("\n")]


star_1_actions = {
    "forward": lambda val, pos, depth: (pos + val, depth),
    "up": lambda val, pos, depth: (pos, depth - val),
    "down": lambda val, pos, depth: (pos, depth + val),
}
star_2_actions = {
    "forward": lambda val, pos, depth, aim: (pos + val, depth - (aim * val), aim),
    "up": lambda val, pos, depth, aim: (pos, depth, aim + val),
    "down": lambda val, pos, depth, aim: (pos, depth, aim - val),
}


class MyTestCase(unittest.TestCase):
    def test_star_1(self):
        data = get_input()
        pos = depth = 0
        for (instruction, val_str) in data:
            (pos, depth) = star_1_actions[instruction](int(val_str), pos, depth)
        print(pos * depth)

    def test_star_2(self):
        data = get_input()
        pos = depth = aim = 0
        for (instruction, val_str) in data:
            (pos, depth, aim) = star_2_actions[instruction](int(val_str), pos, depth, aim)
        print(pos * depth)


if __name__ == '__main__':
    unittest.main()
