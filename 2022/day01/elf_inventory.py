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
    args = parser.parse_args()


    elfs = load_calories_from_file(args.filename)

    print(max([elf.get_total_calories() for elf in elfs])) 


if __name__ == "__main__":
    main()
