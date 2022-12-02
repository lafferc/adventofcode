from typing import List
import argparse

class Elf:
    def __init__(self):
        self.inventory = []

    def add_item(self, calories: int):
        self.inventory.append(calories)

    def get_total_calories(self):
        return sum(self.inventory)



def load_calories_from_file(filename: str) -> List[Elf]:
    elfs = []
    with open(filename) as calories_file:
        elf = Elf()
        for line in calories_file.readlines():
            line = line.strip()
            if not len(line):
                elfs.append(elf)
                elf = Elf()
            else:
                elf.add_item(int(line))
        if len(elf.inventory):
            elfs.append(elf)
    return elfs



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file with elf's calories")
    parser.add_argument("-n", "--num", type=int, default=1, help="number of elfs to print")
    args = parser.parse_args()

    if args.num <= 0:
        raise ValueError("num must be greater than 0")


    elfs = load_calories_from_file(args.filename)

    elfs_calories = [elf.get_total_calories() for elf in elfs]
    elfs_calories.sort(reverse=True)

    print(sum(elfs_calories[:args.num]))




if __name__ == "__main__":
    main()
