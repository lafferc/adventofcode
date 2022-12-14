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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")
    
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)


    index = 0
    total = 0
    for packeta_raw, packetb_raw in load_packets(args.filename):
        packeta = json.loads(packeta_raw)
        packetb = json.loads(packetb_raw)

        index += 1
        logging.debug(f"== Pair {index} ==")
        if (compare_list(packeta, packetb)) < 0:
            logging.debug(f'inputs are in the right order')
            total += index

    print(f"total: {total}")


if __name__ == "__main__":
    main()
