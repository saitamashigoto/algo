#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#  3. INTEGER n
#


def solve(p, q, n):
    m = 10**9 + 7
    cos_n_theta, sin_n_theta = power(q, p, n, m)
    if sin_n_theta % cos_n_theta == 0:
        return (sin_n_theta//cos_n_theta) % m
    a = sin_n_theta
    b = cos_n_theta
    return (a*modInverse(b, m)) % m

def power(a, b, k, m):
    X, Y = 1, 0
    a = a % m
    b = b % m
    while (k > 0):
        if ((k & 1) == 1):
            p = ((X*a) - (Y*b)) % m
            q = ((X*b) + (Y*a)) % m
            X, Y = p, q
        k = k >> 1
        x = ((a*a) - (b*b)) % m
        y = (2*a*b) % m
        a, b = x, y
    return X, Y


def modInverse(a, m):
	m0 = m
	y = 0
	x = 1

	if (m == 1):
		return 0

	while (a > 1):

		q = a // m

		t = m

		m = a % m
		a = t
		t = y

		y = x - q * y
		x = t

	if (x < 0):
		x = x + m0

	return x
    

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(p, q, n)

        fptr.write(str(result) + '\n')

    fptr.close()
