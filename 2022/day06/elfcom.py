from typing import List, Tuple, Dict
import argparse
import logging

def load_file(filename: str) -> str:
    with open(filename) as input_file:
        return input_file.read()


def get_start_of_packet_marker(data: str) -> int:
    """ return the start-of-packet marker index """

    logging.debug("data: %r" % data)
    for i in range(4, len(data)):
        logging.debug(f"i:{i}, {data[i-4:i]}")
        if len(set(data[i-4:i])) == 4:
            return i
    logging.error("End of data")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")
    
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    data = load_file(args.filename)

    marker = get_start_of_packet_marker(data)

    print(marker)

if __name__ == "__main__":
    main()
