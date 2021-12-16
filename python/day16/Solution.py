import unittest


def get_input():
    filename = "input"
    with open(filename, 'r') as file:
        data = file.read().strip()
    # data = "D2FE28"
    # data = "38006F45291200"
    # data = "EE00D40C823060"
    # data = "8A004A801A8002F478"
    # data = "620080001611562C8802118E34"
    # data = "C0015000016115A2E0802F182340"
    # data = "A0016C880162017C3686B18A3D4780"
    # data = "C200B40A82"
    # data = "04005AC33890"
    # data = "880086C3E88112"
    # data = "CE00C43D881120"
    # data = "D8005AC2A8F0"
    # data = "F600BC2D8F"
    # data = "9C005AC2F8F0"
    # data = "9C0141080250320F1802104A08"
    return bin(int(data, 16))[2:].zfill(len(data) * 4)


def get_num(data, i, length):
    return int(data[i:i + length], 2), i + length


def get_bits(data, i, length):
    return data[i:i + length], i + length


def read_packet(data, packets_limit=1000):
    i = 0
    packet_count = 0
    version_sum = 0
    _sum, _prod, _min, _max, _gt, _lt, _eq, res = 0, 1, 10000000000000, - 10000000000000, 0, 0, 0, 0
    prev = 0
    while i < len(data):
        (version, i) = get_num(data, i, 3)
        version_sum += version
        (type, i) = get_num(data, i, 3)
        if type == 4:
            rep = ""
            while i < len(data) and data[i] != '0':
                (add, i) = get_bits(data, i, 5)
                rep += add[1:]
            (add, i) = get_bits(data, i, 5)
            rep += add[1:]
            res = int(rep, 2)
        else:
            (length_type, i) = get_num(data, i, 1)
            if length_type == 0:
                (sub_length, i) = get_num(data, i, 15)
                _i, _version_sum, content, _ = read_packet(data[i:i+sub_length])
                i += _i
                version_sum += _version_sum
            else:
                (packets_num, i) = get_num(data, i, 11)
                _i, _version_sum, content, _ = read_packet(data[i:], packets_num)
                i += _i
                version_sum += _version_sum
            res = content[type]
        _sum, _prod = _sum + res, _prod * res
        _max, _min = max(_max, res), min(_min, res)
        if packet_count == 1:
            _gt, _lt, _eq = int(prev > res), int(prev < res), int(prev == res)
        prev = res
        packet_count += 1
        if packet_count == packets_limit:
            break
    return i, version_sum, (_sum, _prod, _min, _max, 0, _gt, _lt, _eq), res


class MyTestCase(unittest.TestCase):

    def test_star_1(self):
        data = get_input()
        (_, version_sum, _, _) = read_packet(data, 1)
        print("Part 1:", version_sum)

    def test_star_2(self):
        data = get_input()
        (_, _, _, res) = read_packet(data, 1)
        print("Part 1:", res)


if __name__ == '__main__':
    unittest.main()
