#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#  5. INTEGER e
#  6. INTEGER f
#  7. INTEGER g
#  8. INTEGER h
#  9. LONG_INTEGER n
#

x_dict = {}
y_dict = {}
signature_dict = dict()

def solve(a, b, c, d, e, f, g, h, n):
    signature = (a,b,c,d,e,f,g,h)
    global signature_dict, x_dict, y_dict
    if signature in signature_dict:
        x_dict = signature_dict[signature][0]
        y_dict = signature_dict[signature][1]
    else:
        x_dict = {}
        y_dict = {}
        signature_dict[signature] = [x_dict,y_dict]
    result =  calculate(n, signature)
    return result

def calculate(n, signature):
    a,b,c,d,e,f,g,h = signature
    if n in x_dict:
        x = x_dict[n]
    else:
        x = calculate_x(n, signature)
    if n in y_dict:
        y = y_dict[n]
    else:
        y = calculate_y(n, signature)
    return [x % (10**9), y % (10**9)]

def calculate_x(n, signature):
    global x_dict
    if n < 0:
        return 1
    elif n in x_dict:
        return x_dict[n]
    else:
        a,b,c,d,e,f,g,h = signature
        ans = calculate_x(n-a, signature) + calculate_y(n-b, signature) + calculate_y(n-c, signature) + (n * (d**n))
        x_dict[n] = ans
        return ans

def calculate_y(n, signature):
    global y_dict
    if n < 0:
        return 1
    elif n in y_dict:
        return y_dict[n]
    else:
        a,b,c,d,e,f,g,h = signature
        ans = calculate_y(n-e, signature) + calculate_x(n-f, signature) + calculate_x(n-g, signature) + (n * (h**n))
        y_dict[n] = ans
        return ans



if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        d = int(first_multiple_input[3])

        e = int(first_multiple_input[4])

        f = int(first_multiple_input[5])

        g = int(first_multiple_input[6])

        h = int(first_multiple_input[7])

        n = int(first_multiple_input[8])

        result = solve(a, b, c, d, e, f, g, h, n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
