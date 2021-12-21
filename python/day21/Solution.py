import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        return [int(s[-1]) for s in file.read().strip().split('\n')]


def play(pos):
    scores = [0 for p in pos]
    roll = 0
    while True:
        for i, p in enumerate(pos):
            rolls = 0
            for rollnr in range(3):
                roll += 1
                rolls += (roll - 1) % 100 + 1
            pos[i] = (p - 1 + rolls) % 10 + 1
            scores[i] += pos[i]
            if any(p >= 1000 for p in scores):
                return roll, scores


def score_counts(cache, pos0, pos1, score0, score1):
    if (pos0, pos1, score0, score1) in cache:
        return cache[(pos0, pos1, score0, score1)]
    if score0 >= 21:
        return 1, 0
    if score1 >= 21:
        return 0, 1
    scores = (0, 0)
    for roll1 in range(3):
        for roll2 in range(3):
            for roll3 in range(3):
                next_pos0 = (pos0 + roll1 + roll2 + roll3 + 3) % 10
                next_score0 = score0 + next_pos0 + 1
                next0, next1 = score_counts(cache, pos1, next_pos0, score1, next_score0)  # memoized call with swap
                scores = (scores[0] + next1, scores[1] + next0)
    cache[(pos0, pos1, score0, score1)] = scores
    return scores


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        pos = get_input()
        roll, scores = play(pos)
        print("Part 1:", roll * min(scores))

    def test_star_2(self):
        pos = get_input()
        print("Part 2:", max(score_counts({}, pos[0] - 1, pos[1] - 1, 0, 0)))


if __name__ == '__main__':
    unittest.main()
