import argparse
import logging
import re
from typing import List

g_max_blue = 14
g_max_green = 13
g_max_red = 12

class CubeSet:
    blue = 0
    red = 0
    green = 0
    def __init__(self, description):
        logging.debug(description)
        for part in description.split(','):
            count, colour = part.split()
            setattr(self, colour, int(count))

class CubeGame:
    def __init__(self, description):
        self._id = None
        self.rounds = []
        self.parse_desription(description)

    def is_valid(self):
        for r in self.rounds:
            if (r.blue > g_max_blue
                    or r.red > g_max_red
                    or r.green > g_max_green):
                return False
        return True

    def parse_desription(self, description):
        game, rounds = description.split(':')
        logging.debug(game)
        self._id = int(game.split()[1])
        for r in rounds.split(';'):
            self.rounds.append(CubeSet(r))



def load_file(filename: str) -> List[CubeGame]:
    with open(filename) as input_file:
        for line in input_file.readlines():
            yield CubeGame(line.strip())



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument("-d", "--debug", help="set debug logging", action="store_true")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    games = load_file(args.filename)
    print(sum([cg._id for cg in games if cg.is_valid()]))


if __name__ == "__main__":
    main()
