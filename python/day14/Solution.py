import unittest
from collections import Counter, defaultdict
from copy import copy


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        result = file.read().strip().split("\n\n")
        rules = {k: v for (k, v) in [s.split(" -> ") for s in result[1].split("\n")]}
        return result[0], rules


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        steps = 10
        (polymer, rules) = get_input()
        for _ in range(steps):
            enriched = ''
            for pos in range(len(polymer)):
                enriched += polymer[pos]
                enriched += rules[polymer[pos:pos+2]] if polymer[pos:pos+2] in rules else ''
            polymer = enriched
        frequencies = Counter(polymer).most_common()
        print("Part 1:", frequencies[0][1] - frequencies[-1][1])

    def test_star_2(self):
        steps = 40
        (polymer, rules) = get_input()

        single_counts = defaultdict(int)
        for c in polymer:
            single_counts[c] += 1

        pair_counts = defaultdict(int)
        for pos in range(len(polymer)-1):
            pair_counts[polymer[pos:pos+2]] += 1

        for _ in range(steps):
            for (pair, count) in copy(pair_counts).items():
                if pair in rules:
                    single_counts[rules[pair]] += count
                    pair_counts[pair] -= count
                    pair_counts[pair[0] + rules[pair]] += count
                    pair_counts[rules[pair] + pair[1]] += count

        print("Part 2:", max(single_counts.values()) - min(single_counts.values()))


if __name__ == '__main__':
    unittest.main()
