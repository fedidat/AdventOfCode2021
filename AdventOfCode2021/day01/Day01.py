import unittest

def get_input():
    filename = "input"
    # filename = "sample"
    with open(filename, 'r') as file:
        return [int(x) for x in file]

class MyTestCase(unittest.TestCase):
    def test_star_1(self):
        data = get_input()
        print(sum((data[i+1] > data[i] for i in range(0, len(data)-1))))
    def test_star_2(self):
        data = get_input()
        print(sum((data[i+3] > data[i] for i in range(0, len(data)-3))))

if __name__ == '__main__':
    unittest.main()
