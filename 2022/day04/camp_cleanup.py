import argparse


def is_full_overlap(start1: int, end1: int, start2: int, end2: int) -> bool:
    # is 1 inside 2
    if start1 >= start2 and end1 <= end2:
        return True
    # is 2 inside 1
    if start1 <= start2 and end1 >= end2:
        return True
    return False


def is_overlap(start1: int, end1: int, start2: int, end2: int) -> bool:
    if start1 >= start2 and start1 <= end2:
        return True
    if end1 >= start2 and end1 <= end2:
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    args = parser.parse_args()

    full_overlap_count = 0
    overlap_count = 0
    with open(args.filename) as assignments_file:
        for line in assignments_file.readlines():
            line = line.strip()

            if not len(line):
                continue

            elf1, elf2 = line.split(',')

            s1, e1 = elf1.split('-')
            s2, e2 = elf2.split('-')

            if is_full_overlap(int(s1), int(e1), int(s2), int(e2)):
                full_overlap_count += 1
                overlap_count += 1
                continue

            if is_overlap(int(s1), int(e1), int(s2), int(e2)):
                overlap_count += 1

    print(overlap_count)

if __name__ == "__main__":
    main()

