from typing import List, Tuple, Dict
import argparse
import string
import re
import logging


def load_file(filename: str) -> Tuple[List, List]:
    """
       loads the input file and return the contents before and after the blank line
    """
    content = ([], [])
    cur_list = content[0]
    with open(filename) as input_file:
        for line in input_file.readlines():
            if line == "\n":
                cur_list = content[1]
                continue

            # add to list without newline char
            cur_list.append(line[:-1])

    return content


def read_stack_diagram(diagram: List, stacks: Dict):

    # start from the bottom, last line is the descripion of the sacks

    highest_stack = len(diagram)- 1

    for i in range(len(diagram[-1])):
        c = diagram[-1][i]
        if c in list(string.digits):
            stacks[c] = []

            for j in range(highest_stack -1, -1, -1):
                crate = diagram[j][i]
                if crate != ' ':
                    stacks[c].append(diagram[j][i])


def parse_intructions(intructions: List[str]) -> Tuple[int, str, str]:
    pattern = re.compile('move (\d+) from (\d) to (\d)')

    for line in intructions:
        match = pattern.match(line)

        logging.debug(line)
        yield (int(match[1]), match[2], match[3])



def crate_mover_9000(stacks, intructions):
    for n, stack, to in parse_intructions(intructions):
        for i in range(n):
            crate = stacks[stack].pop()
            stacks[to].append(crate)


def crate_mover_9001(stacks, intructions):
    for n, stack, to in parse_intructions(intructions):
        stacks[to].extend(stacks[stack][-n:])
        stacks[stack] = stacks[stack][:-n]
        logging.debug(stacks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")
    
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)


    stacks = {}
    #TODO load stacks and intructions

    diagram, raw_intructions = load_file(args.filename)

    read_stack_diagram(diagram, stacks)


    logging.debug(stacks)

    crate_mover_9001(stacks, raw_intructions)

    logging.debug(stacks)

    code = ''
    for s in stacks.values():
        code += s[-1]

    print(code)


if __name__ == "__main__":
    main()
