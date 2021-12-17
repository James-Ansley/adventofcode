import math
import operator
from dataclasses import dataclass

OPS = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    4: lambda x: next(x),
    5: lambda x: operator.gt(*x),
    6: lambda x: operator.lt(*x),
    7: lambda x: operator.eq(*x),
}


@dataclass
class Bits:
    data: int
    num_bits: int

    def pop(self, n):
        self.num_bits -= n
        value = self.data >> self.num_bits
        self.data &= (2 ** self.num_bits - 1)
        return value


def parse(data):
    version = data.pop(3)
    type_id = data.pop(3)
    packet_data = []

    if type_id == 4:
        literal = 0
        while data.pop(1) == 1:
            literal = (literal << 4) + data.pop(4)
        packet_data.append((literal << 4) + data.pop(4))
    elif data.pop(1) == 1:
        num_packets = data.pop(11)
        packet_data.extend(parse(data) for _ in range(num_packets))
    else:
        num_bits = data.pop(15)
        sub_packet_data = Bits(data.pop(num_bits), num_bits)
        while sub_packet_data.data > 0:
            packet_data.append(parse(sub_packet_data))
    return version, type_id, packet_data


def sum_versions(packet):
    version, type_id, packet_data = packet
    if type_id != 4:
        return version + sum(sum_versions(p) for p in packet_data)
    return version


def evaluate(packet):
    if isinstance(packet, int):
        return packet
    op = OPS[packet[1]]
    return op(evaluate(p) for p in packet[2])


with open('input_files/day16') as f:
    data = f.read().strip()

bits = Bits(int(data, 16), len(data) * 4)
packets = parse(bits)

print(sum_versions(packets))
print(evaluate(packets))
