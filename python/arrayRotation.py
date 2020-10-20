#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    print(a)
    print(d)
    # a is the array, d is the number of rotations
    counter = 0
    while counter < d:
        a.append(a.pop(0))
        counter = counter + 1
        print(f"Step {counter}: {a}")
    return a


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(' '.join(list(map(str, result))))
