import math
import operator

OPS = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: operator.gt(*x),
    6: lambda x: operator.lt(*x),
    7: lambda x: operator.eq(*x),
}


class Bits:
    def __init__(self, value, bits):
        self.bits = bits
        self.data = value

    def pop(self, n):
        value = self.data >> self.bits - n
        self.bits -= n
        self.data = self.data & (2 ** self.bits - 1)
        return value


def parse(data):
    version = data.pop(3)
    type_id = data.pop(3)
    if type_id == 4:
        literal = 0
        while data.pop(1) == 1:
            literal <<= 4
            literal += data.pop(4)
        return version, type_id, (literal << 4) + data.pop(4)

    if data.pop(1) == 1:
        num_packets = data.pop(11)
        sub_packets = [parse(data) for _ in range(num_packets)]
    else:
        num_bits = data.pop(15)
        sub_packet_data = Bits(data.pop(num_bits), num_bits)
        sub_packets = []
        while sub_packet_data.data > 0:
            sub_packets.append(parse(sub_packet_data))
    return version, type_id, sub_packets


def sum_versions(packet):
    if isinstance(packet, tuple) and isinstance(packet[2], list):
        return packet[0] + sum(sum_versions(p) for p in packet[2])
    return packet[0]


def evaluate(packet):
    _, type_id, packet_data = packet
    if type_id == 4:
        return packet[2]
    op = OPS[type_id]
    return op(evaluate(p) for p in packet_data)


with open('input_files/day16') as f:
    data = f.read().strip()

bits = Bits(int(data, 16), len(data) * 4)
packets = parse(bits)

print(sum_versions(packets))
print(evaluate(packets))
