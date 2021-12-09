#!/usr/bin/env python

# Build a string from each column and then use
# Counter(string) and it will count the 1s and 0s

from collections import Counter

def main():
    # Define the dictionary we are going to use
    line_d = {}
    newLine_d = {}
    lineN = 1
    posN = 0
    workLine = ''
    buildLine = ''

    f = open('day3-input-short.txt', 'r')
    #f = open('day3-input.txt', 'r')

    # Build the line dictionary
    for line in f:
        line_d[lineN] = line
        lineN += 1

    print(line_d)

    # Cycle through every position
    while posN < len(line)-1:
        # Build the string for column in posN
        for key in line_d:
            workLine = line_d[key]
            buildLine = buildLine+workLine[posN]

        print(buildLine)

        # Count the digits in the string to find out the most common
        element = Counter(buildLine)
        if element['1'] < element['0']:
            toKeep = 0
        else:
            toKeep = 1

        print('We are keeping: ', toKeep, 'at position: ', posN)

        # Build the new dictionary
        for key in line_d:
            if line_d[key][posN] == str(toKeep):
                newLine_d[key] = line_d[key]

        line_d = newLine_d
        print(line_d)

        if len(line_d.keys()) == 1: break

        posN += 1
        buildLine = ''
        newLine_d = {}

#    # Calculate gama and epsilon
#    gamaDecimal = int(gama, 2)
#    epsilonDecimal = int(epsilon, 2)
#
#    print(gamaDecimal)
#    print(epsilonDecimal)
#
#    print(gamaDecimal*epsilonDecimal)

    f.close()

if __name__ == "__main__":
    main()