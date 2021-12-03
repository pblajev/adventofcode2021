#!/usr/bin/env python


def main():
    pnum = 0
    countnum = 0
    f = open('day1-input.txt', 'r')
    for line in f:
        num = int(line)
        if num > pnum:
            if pnum != 0: countnum += 1
        pnum = num

    print('I got', countnum)

    f.close()

if __name__ == '__main__':
    main()