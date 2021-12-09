#!/usr/bin/env python

# Build a string from each column and then use
# Counter(string) and it will count the 1s and 0s

from collections import Counter

def main():
    # Define the dictionary we are going to use
    collector_d = {}
    lineN = 1
    gama = ''
    epsilon = ''

    #f = open('day3-input-short.txt', 'r')
    f = open('day3-input.txt', 'r')
    for line in f:
        posN = 0

        #print('Line: ', line)

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

    #print(collector_d)

    # Build gama and epsilon
    for k in collector_d:
        element=Counter(collector_d[k])
        if element['1'] > element['0']:
            gama = gama+'1'
            epsilon = epsilon+'0'
        else:
            gama = gama+'0'
            epsilon = epsilon+'1'

    print(gama)
    print(epsilon)

    # Calculate gama and epsilon
    gamaDecimal = int(gama, 2)
    epsilonDecimal = int(epsilon, 2)

    print(gamaDecimal)
    print(epsilonDecimal)

    print(gamaDecimal*epsilonDecimal)

    f.close()

if __name__ == "__main__":
    main()