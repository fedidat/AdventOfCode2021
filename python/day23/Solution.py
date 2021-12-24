import unittest
from functools import lru_cache


def get_input(part2):
    # filename = "sample"
    filename = "input"
    p2 = """  #D#C#B#A#
  #D#B#A#C#"""
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n')
    if part2:
        data[-2:-2] = p2.split('\n')
    return tuple(map(tuple, zip(*[[s[i*2+1] for i in range(1, 5)] for s in data[2:-1]])))


def least_cost(lines, room_map, hall_spots, destination, costs):
    room_size = len(lines[0])

    @lru_cache(maxsize=None)
    def best_cost(hall, rooms):
        if rooms == (("A",) * room_size, ("B",) * room_size, ("C",) * room_size, ("D",) * room_size):
            return 0  # solved, no cost from here
        result = float('inf')
        for i, square in enumerate(hall):  # move from the hallway into a room
            if square is None:
                continue  # free hallway spot, ignore
            dst = destination[square]
            if any(roommate is not None and roommate != square for roommate in rooms[dst]):
                continue  # foreigner in room
            offset = 1 if room_map[dst] > i else -1
            if any(spot is not None for spot in hall[i + offset:room_map[dst] + offset:offset]):
                continue  # hallway busy ahead
            none_count = sum(elem is None for elem in rooms[dst])
            new_room = (None,) * (none_count - 1) + (square,) * (room_size - none_count + 1)
            steps = none_count + abs(i - room_map[dst])
            step_cost = steps * costs[square]
            best_sub_cost = step_cost + best_cost(hall[:i] + (None,) + hall[i + 1:], rooms[:dst] + (new_room,) + rooms[dst + 1:])
            result = min(result, best_sub_cost)
        for i, room in enumerate(rooms):  # move from a room into the hallway
            if not any(elem is not None and destination[elem] != i for elem in room):
                continue  # if nothing needs to move from room, ignore
            none_count = sum(elem is None for elem in room)
            steps = none_count + 1
            square = room[none_count]
            for hall_dst in hall_spots:
                dst_steps = steps + abs(hall_dst - room_map[i])
                dst_cost = dst_steps * costs[square]
                if any(spot is not None for spot in hall[min(hall_dst, room_map[i]): max(hall_dst, room_map[i]) + 1]):
                    continue  # hallway busy ahead
                new_room = (None,) * (none_count + 1) + room[none_count + 1:]
                best_sub_cost = dst_cost + best_cost(hall[:hall_dst] + (square,) + hall[hall_dst + 1:], rooms[:i] + (new_room,) + rooms[i + 1:])
                result = min(result, best_sub_cost)
        return result

    hall_start = tuple(None for _ in range(len(room_map) + len(hall_spots)))
    return best_cost(hall_start, lines)


class MyTestCase(unittest.TestCase):
    room_map = (2, 4, 6, 8)
    hall_spots = (0, 1, 3, 5, 7, 9, 10)
    destination = {"A": 0, "B": 1, "C": 2, "D": 3}
    costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

    def test_star_1(self):
        rooms = get_input(False)
        print("Part 1:", least_cost(rooms, self.room_map, self.hall_spots, self.destination, self.costs))

    def test_star_2(self):
        rooms = get_input(True)
        print("Part 2:", least_cost(rooms, self.room_map, self.hall_spots, self.destination, self.costs))


if __name__ == '__main__':
    unittest.main()
