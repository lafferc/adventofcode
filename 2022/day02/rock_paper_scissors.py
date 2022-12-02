from typing import List, Tuple
import argparse

g_points_map = {
        #        +1      +2      +3
        #       Rock    Paper   Scissors
        "A" : { "X": 4, "Y": 8, "Z": 3},   # Rock
        "B" : { "X": 1, "Y": 5, "Z": 9},   # Paper
        "C" : { "X": 7, "Y": 2, "Z": 6},   # Scissors
}

def load_file(filename: str) -> List[Tuple[str, str]]:
    rounds = []
    with open(filename) as strategy_file:
        for line in strategy_file.readlines():
            line = line.strip()

            if not len(line):
                continue

            rounds.append(line.split())
    return rounds



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    args = parser.parse_args()


    rounds = load_file(args.filename)

    points = 0
    for opponent, player in rounds:
        points += g_points_map[opponent][player]

    print(points)


if __name__ == "__main__":
    main()
