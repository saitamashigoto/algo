#!/bin/python3

import math
import os
import random
import re
import sys


def larrysArray(A):
    length = len(A)
    u_i = 0
    while u_i < length:
        if A[u_i] != u_i+1:
            t_i = A.index(u_i+1)
            r_i = t_i - 2
            if r_i < u_i:
                if (t_i+1) >= length:
                    break
                r_i = t_i - 1
            rotate(A, r_i)
        else:
            u_i += 1
    if u_i == length:
        return "YES"
    else:
        return 'NO'

def rotate(A, i):
    e_i = A[i]
    A[i] = A[i+1]
    A[i+1] = A[i+2]
    A[i+2] = e_i

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
