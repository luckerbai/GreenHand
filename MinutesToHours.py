#!/usr/bin/env python3

import sys

def Hours(minutes):
    if int(minutes) > 0:
        print("{} H, {} M".format(int(minutes)//60, int(minutes)%60))

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            Hours(sys.argv[1])

    except:
        print("ValueError")
