#!/usr/bin/env python

def main():
    pnum = 0
    countnum = 0
    f = open('day1-input.txt', 'r')

    # build a list
    numbers_l = []
    for line in f:
        numbers_l.append(line)

    starttrio = 0
    prevTriosum = 0
    while starttrio < len(numbers_l) - 2:
        Triosum = int(numbers_l[starttrio]) + int(numbers_l[starttrio + 1]) \
                  + int(numbers_l[starttrio + 2])

        if prevTriosum != 0 and Triosum > prevTriosum: countnum += 1
        prevTriosum = Triosum

        starttrio += 1

    print(countnum)
    f.close()

if __name__ == '__main__':
    main()