from typing import List, Tuple
import argparse
import string


stacks = {
        "1": ["z","N"],
        "2": ["M", "C", "D"],
        "3": ["P"],
        }

intructions = [
        (1, "2", "1"),
        (3, "1", "3"),
        (2, "2", "1"),
        (1, "1", "2"),
        ]
              

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    # args = parser.parse_args()


    #TODO load stacks and intructions

    print(stacks)

    for n, stack, to in intructions:
        #print(f"move {n} from {stack} to {to}")
        for i in range(n):
            crate = stacks[stack].pop()
            #print("moving %s" % crate)
            stacks[to].append(crate)

    print(stacks)


if __name__ == "__main__":
    main()
