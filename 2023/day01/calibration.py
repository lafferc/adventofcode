import argparse
import logging
from typing import List

def load_file(filename: str) -> List:
    with open(filename) as input_file:
        for line in input_file.readlines():
            yield line.strip()


def extract_digits(inlist):
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


g_valid_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }

def extract_numbers(inlist):
    for line in inlist:
        first_digit = None
        last_digit = None
        logging.debug(f"{line} - {len(line)}")
        for i in range(len(line)):
            logging.debug(f"{i}: {line[i]}")

            if line[i].isdigit():
                first_digit = line[i]
                break
            for num in g_valid_numbers.keys():
                if line[i:].startswith(num):
                    first_digit = g_valid_numbers[num]
                    break
            if first_digit is not None:
                break

        for i in range(len(line) - 1, -1, -1):
            logging.debug(f"{i}: {line[i]}")

            if line[i].isdigit():
                last_digit = line[i]
                break

            for num in g_valid_numbers.keys():
                if line[i:].startswith(num):
                    last_digit = g_valid_numbers[num]
                    break
            if last_digit is not None:
                break


        yield int(first_digit + last_digit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    print(sum(extract_numbers(load_file(args.filename))))


if __name__ == "__main__":
    main()
