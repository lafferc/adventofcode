from typing import List, Tuple
import argparse
import string


g_priorities_order = '_' + string.ascii_lowercase + string.ascii_uppercase


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

    def get_all_items(self):
        return self.compartments[0] + self.compartments[1]


def load_items(filename: str) -> List[str]:
    items = []
    with open(filename) as strategy_file:
        for line in strategy_file.readlines():
            line = line.strip()

            if not len(line):
                continue

            items.append(line)
    return items


def find_duplicate_items_total_value(rucksacks: List[Rucksack]) -> int:
    total = 0
    for r in rucksacks:
        for item in r.get_duplicate_items():
            total += g_priorities_order.index(item)
    return total


def find_badge_item(r1: Rucksack, r2: Rucksack, r3: Rucksack) -> str:
    s1 = set(r1.get_all_items())
    s2 = set(r2.get_all_items())
    s3 = set(r3.get_all_items())

    badge = list(s1.intersection(s2, s3))

    assert len(badge) == 1

    return badge[0]


def find_badge_items_total_value(rucksacks: List[Rucksack]) -> int:
    total = 0
    for i in range(0, len(rucksacks), 3):
        item = find_badge_item(*rucksacks[i:i+3])
        total += g_priorities_order.index(item)
    return total


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

    # print(find_duplicate_items_total_value(rucksacks))

    print(find_badge_items_total_value(rucksacks))




if __name__ == "__main__":
    main()
