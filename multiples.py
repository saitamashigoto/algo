#!/bin/python3

import math
import os
import random
import re
import sys


def closestNumber(a, b, x):
    power = (a**b)
    number = (power / x)
    xf = math.floor(number) * x
    xc = math.ceil(number) * x
    return  xf if power - xf <= xc - power else xc

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        x = int(first_multiple_input[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
