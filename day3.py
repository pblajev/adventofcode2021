#!/usr/bin/env python

from collections import Counter

def main():
    f = open('day3-input-short.txt', 'r')

    lineN = 0
    collector_d = {}

    for line in f:
        lineN += 1
        posN = 0
        print('For line ', line)
        print(Counter(line))
        break

        # Iterate through the line string
        while posN < len(line)-1:

            # Build the dictionary
            if line[posN] == '0':
                collector_d['l'+str(lineN)+'p'+str(posN)+'0'] = 1
                collector_d['l'+str(lineN)+'p'+str(posN)+'1'] = 2
            else:
                collector_d['l'+str(lineN)+'p'+str(posN)+'0'] = 2
                collector_d['l'+str(lineN)+'p'+str(posN)+'1'] = 1

            print("Position ", posN, "is ", line[posN])
            posN += 1

    print(collector_d.items())
if __name__ == "__main__":
    main()