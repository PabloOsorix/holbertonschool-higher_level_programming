#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        sum += int(sys.argv[i])
    print(sum)
