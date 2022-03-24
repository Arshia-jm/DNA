# Use libraries

import csv
import re
from sys import argv, exit

# The main function


def main():
    # Print the error if the input arguments are not acceptable
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
    # Else the main program will run

    else:
        dna(argv)

# The main code is written in this


def dna(argv):
    with open(argv[1], newline="") as csvfile:
        database_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for i, row in enumerate(database_reader):
            if i != 0:
                list_database_strs = list(map(int, row[1:]))
                if list_database_strs == longest_strs:
                    print(row[0])
                    break
            else:
                with open(argv[2], "r") as txtfile:
                    line = next(txtfile)
                    longest_strs = []
                    for i in range(1, len(row)):
                        pattern = row[i]
                        matches = (
                            match[0] for match in re.finditer(fr"(?:{pattern})+", line)
                        )
                        try:
                            longest = int(len(max(matches, key=len)) / len(pattern))
                            longest_strs.append(longest)
                        except ValueError:
                            longest_strs.append(0)
        else:
            print("No match")


main()
