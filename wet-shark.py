#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    start = 2
    predict = start + (s-1)*2
    if predict < 42:
        return predict
    n42 = predict//42
    while n42 > 0:
        start = predict +  2
        if start % 42 == 0:
            start += 2
        predict = start + (n42-1)*2
        n42 = predict//42 - start//42
    return predict%(10**9+7)


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        s = int(input().strip())

        result = solve(s)

        fptr.write(str(result) + '\n')

    fptr.close()
