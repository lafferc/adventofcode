from typing import List, Tuple
import argparse



## Rock +1
## Paper +2
## Scissors +3
g_points_map = {
        #        0       3       6
        #       Lose    Draw    Win
        "A" : { "X": 3, "Y": 4, "Z": 8},   # Rock
        "B" : { "X": 1, "Y": 5, "Z": 9},   # Paper
        "C" : { "X": 2, "Y": 6, "Z": 7},   # Scissors
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
