from typing import List, Tuple
import argparse
import string


class Rucksack:
    def __init__(self):
        self.compartments = [[], []]

    def pack(self, items: List):
        n = int((len(items))/2)
        self.compartments[0] = items[:n]
        self.compartments[1] = items[n:]

    def get_duplicate_items(self):
        c1 = set(self.compartments[0])
        c2 = set(self.compartments[1])

        return list(c1.intersection(c2))


def load_items(filename: str) -> List[str]:
    items = []
    with open(filename) as strategy_file:
        for line in strategy_file.readlines():
            line = line.strip()

            if not len(line):
                continue

            items.append(line)
    return items


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    args = parser.parse_args()

    priorities_order = '_' + string.ascii_lowercase + string.ascii_uppercase

    rucksacks = []
    items = load_items(args.filename)

    for items_str in items:
        r = Rucksack()
        r.pack(list(items_str))
        rucksacks.append(r)

    total = 0
    for r in rucksacks:
        for item in r.get_duplicate_items():
            total += priorities_order.index(item)

    print(total)


if __name__ == "__main__":
    main()
