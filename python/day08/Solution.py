import unittest


def get_input():
    # filename = "sample"
    filename = "input"
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")
        return [[[''.join(sorted(d)) for d in p.strip().split(" ")] for p in line.split("|")] for line in lines]


class MyTestCase(unittest.TestCase):
    def test_star_1(self):
        data = get_input()
        print("Part 1:", sum(sum(len(d) in [2, 3, 4, 7] for d in l[1]) for l in data))

    def test_star_2(self):
        data = get_input()
        output_sum = 0
        for line in data:
            digit = {k: next(d for d in line[0] if len(d) == v) for (k, v) in {1: 2, 7: 3, 4: 4, 8: 7}.items()}

            d_0_6_9 = [d for d in line[0] if len(d) == 6]
            digit[6] = next(d for d in d_0_6_9 if len([c for c in d if c in digit[1]]) == 1)
            digit[0] = next(d for d in d_0_6_9 if d != digit[6] and next(c for c in digit[8] if c not in d) in digit[4])
            digit[9] = next(d for d in d_0_6_9 if d != digit[6] and d != digit[0])

            d_2_3_5 = [d for d in line[0] if len(d) == 5]
            digit[5] = next(d for d in d_2_3_5 if len([c for c in digit[6] if c not in d]) == 1)
            digit[3] = next(d for d in d_2_3_5 if len([c for c in d if c not in digit[5]]) == 1)
            digit[2] = next(d for d in d_2_3_5 if d != digit[3] and d != digit[5])

            signal_to_digit = {v: k for k, v in digit.items()}
            output = [str(signal_to_digit[d]) for d in line[1]]
            output_sum += int(''.join(output))
        print("Part 2:", output_sum)


if __name__ == '__main__':
    unittest.main()
