#!/usr/bin/env python

def main():
    positionX, positionY, aim = 0, 0, 0
    errorFound = 0
    f = open('day2-input.txt', 'r')

    for line in f:
        line_l = line.split()

        if line_l[0] == 'forward':
            positionX = positionX + int(line_l[1])
            positionY = positionY + (aim * int(line_l[1]))
        elif line_l[0] == 'down':
            aim = aim + int(line_l[1])
        elif line_l[0] == 'up':
            aim = aim - int(line_l[1])
        else:
            errorFound = 1

        if errorFound:
            print('WTF')
            break

    print(positionX * positionY)
    f.close()

if __name__ == '__main__':
    main()