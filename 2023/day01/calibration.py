import argparse
import logging
from typing import List

def load_file(filename: str) -> List:
    with open(filename) as input_file:
        return input_file.readlines()


def extract_values(inlist):
    for line in inlist:
        first_digit = None
        last_digit = None
        for c in line:
            if c.isdigit():
                first_digit = c
                break
        for c in line[::-1]:
            if c.isdigit():
                last_digit = c
                break
        logging.debug(first_digit + last_digit)
        yield int(first_digit + last_digit)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    print(sum(extract_values(load_file(args.filename))))


if __name__ == "__main__":
    main()
