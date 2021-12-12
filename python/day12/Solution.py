import unittest
from copy import copy


def get_input():
    # filename = "sample"
    # filename = "sample2"
    # filename = "sample3"
    filename = "input"
    with open(filename, 'r') as file:
        return [s.split("-") for s in file.read().strip().split("\n")]


def get_neighbors(data):
    neighbors = {}
    for src, dst in data:
        neighbors.setdefault(src, []).append(dst)
        neighbors.setdefault(dst, []).append(src)
    return neighbors


def traverse(neighbors, path, visited, result, allowed):
    if path[-1] == "end":
        result.add(','.join(path))
        return
    if path[-1] in visited:
        return
    if path[-1].islower():
        if path[-1] in allowed:
            allowed.remove(path[-1])
        else:
            visited.append(path[-1])
    for neighbor in neighbors[path[-1]]:
        traverse(neighbors, path + [neighbor], copy(visited), result, copy(allowed))


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        neighbors = get_neighbors(get_input())
        result = set()
        traverse(neighbors, ["start"], [], result, [])
        print("Part 1:", len(result))

    def test_star_2(self):
        neighbors = get_neighbors(get_input())
        small_caves = [s for s in neighbors.keys() if s.islower() and s not in ["start", "end"]]
        result = set()
        for small_cave in small_caves:
            traverse(neighbors, ["start"], [], result, [small_cave])
        print("Part 2:", len(result))


if __name__ == '__main__':
    unittest.main()
