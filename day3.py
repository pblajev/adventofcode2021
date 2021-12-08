#!/usr/bin/env python

# Build a string from each column and then use
# Counter(string) and it will count the 1s and 0s

from collections import Counter

def main():
    # Define the dictionary we are going to use
    collector_d = {}
    lineN = 1

    f = open('day3-input-short.txt', 'r')
    for line in f:
        posN = 0

        # Iterate through the line string
        while posN < len(line)-1:
            # Build the strings from each column
            if lineN == 1:
                # Empty dictionary
                collector_d[posN] = line[posN]
            else:
                collector_d[posN] = collector_d[posN]+line[posN]
            posN += 1

        lineN +=1

    print(collector_d)
if __name__ == "__main__":
    main()