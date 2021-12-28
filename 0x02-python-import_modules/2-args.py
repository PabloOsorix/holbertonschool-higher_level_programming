#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    for i in range(len(sys.argv)):
        if len(sys.argv) == 1:
            print(f"{i} arguments.")
        if i == 0:
           continue
        
        if len(sys.argv) == 2:
            if count == 0:
                print(f"{len(sys.argv) - 1} argument:")
            count = 1
        if len(sys.argv) > 1:
            if count == 0:
                print(f"{len(sys.argv) - 1} arguments:")
            print(f"{i}: {sys.argv[i]}")
            count = 1
