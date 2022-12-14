import argparse
import logging
import json

def load_packets(filename: str):
    """
       loads the input file and return the contents before and after the blank line
    """

    packets = []
    with open(filename) as input_file:
        for line in input_file.readlines():
            if line == "\n":
                yield packets
                packets = []
                continue

            packets.append(line[:-1])

    yield packets


def compare_list(a, b):
    logging.debug(f"compare {a} vs {b}")
    r = 0
    for i in range(max(len(a), len(b))):
        if i == len(a):
            return -1
        elif i == len(b):
            return 1

        if type(a[i]) == type(b[i]):
            if type(a[i]) is list:
                r = compare_list(a[i], b[i])
            elif type(a[i]) is int:
                r = a[i] - b[i]
                logging.debug(f'Compare {a[i]} vs {b[i]}')
        else:
            if type(a[i]) is int:
                logging.debug(f'convert {a[i]} to list {[a[i]]}')
                r = compare_list([a[i]], b[i])
            else:
                logging.debug(f'convert {b[i]} to list {[b[i]]}')
                r = compare_list(a[i], [b[i]])
        if r != 0:
            return r
    return r


class Packet:
    def __init__(self, raw: str):
        self.raw = raw
        self.data = json.loads(raw)

    def __eq__(self, other):
        return compare_list(self.data, other.data) == 0

    def __lt__(self, other):
        return compare_list(self.data, other.data) < 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")
    
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)


    packets = []
    for packeta_raw, packetb_raw in load_packets(args.filename):
        packets.append(Packet(packeta_raw))
        packets.append(Packet(packetb_raw))


    divider1 = Packet("[[2]]")
    divider2 = Packet("[[6]]")

    packets.append(divider1)
    packets.append(divider2)

    logging.debug("==== start of sort ====")
    packets.sort()
    logging.debug("==== end of sort ====")

    if args.debug:
        for p in packets:
            print(p.raw)
            if p.raw in [divider1.raw, divider2.raw]:
                print("^^^^")

    index_div1 = packets.index(divider1) + 1 
    index_div2 = packets.index(divider2) + 1

    print(f"{index_div1} x {index_div2} = {index_div2*index_div1}")


if __name__ == "__main__":
    main()
