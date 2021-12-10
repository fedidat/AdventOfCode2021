import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return [s for s in file.read().strip().split("\n")]


openers = {'[': ']', '(': ')', '<': '>', '{': '}'}
checker_score_map = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
autocomplete_score_map = {')': 1, ']': 2, '}': 3, '>': 4, None: 0}


def syntax_check(line):
    tokens = []
    for c in line:
        if c in openers:
            tokens.append(c)
        elif c == openers[tokens[-1]]:
            tokens.pop()
        else:
            return tokens, c
    return tokens, None


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        total = 0
        for line in data:
            total += checker_score_map[syntax_check(line)[1]]
        print("Part 1:", total)

    def test_star_2(self):
        data = get_input()
        scores = []
        for line in data:
            tokens, offending = syntax_check(line)
            if offending:
                continue
            score = 0
            while len(tokens) > 0:
                score = 5 * score + autocomplete_score_map[openers[tokens.pop()]]
            scores.append(score)
        print("Part 2:", sorted(scores)[int((len(scores)-1)/2)])


if __name__ == '__main__':
    unittest.main()
