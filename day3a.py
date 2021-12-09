#!/usr/bin/env python

from collections import Counter

def main():
    # Define the dictionary we are going to use
    line_d = {}
    workLine_d = {}
    newLine_d = {}
    lineN = 1
    posN = 0
    buildLine = ''

    #f = open('day3-input-short.txt', 'r')
    f = open('day3-input.txt', 'r')

    # Build the line dictionary
    for line in f:
        line_d[lineN] = line
        lineN += 1

    # Cycle through every position
    for mostleast in ['most', 'least']:
        print()
        print('==> Finding ', mostleast)
        workLine_d = line_d
        print(workLine_d)

        while posN < len(line)-1:
            # Build the string for column in posN
            for key in workLine_d:
                workLine = workLine_d[key]
                buildLine = buildLine+workLine[posN]

            print(buildLine)

            # Count the digits in the string to find out the most common
            element = Counter(buildLine)
            if mostleast == 'most':
                if element['1'] < element['0']:
                    toKeep = 0
                else:
                    toKeep = 1
            else:
                if element['1'] < element['0']:
                    toKeep = 1
                else:
                    toKeep = 0

            print('We are keeping: ', toKeep, 'at position: ', posN)

            # Build the new dictionary
            for key in workLine_d:
                if workLine_d[key][posN] == str(toKeep):
                    newLine_d[key] = workLine_d[key]

            workLine_d = newLine_d
            print(workLine_d)

            posN += 1
            buildLine = ''
            newLine_d = {}

            # Break out of the while loop if we are at the last element
            if len(workLine_d.keys()) == 1:
                if mostleast == 'most':
                    for k in workLine_d: oxygen = workLine_d[k]
                if mostleast == 'least':
                    for k in workLine_d: co2 = workLine_d[k]
                posN = 0
                break

    print('I got oxygen: ', oxygen)
    print('I got    co2: ', co2)

    print(int(oxygen, 2)*int(co2, 2))

    f.close()

if __name__ == "__main__":
    main()