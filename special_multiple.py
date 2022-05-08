#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

permutations = {1: [9], 2: [90, 99]}
list_digit = [1, 2]
found_result = {}

def solve(n):
    global found_result
    if found_result.get(n, False):
        return found_result[n]
    
    i = 1
    while True:
        perm_list = calculate_permutations(i)
        for num in perm_list:
            if num % n == 0:
                return str(num)
        i += 1

def calculate_permutations(n_digits):
    global permutations, list_digit

    if n_digits not in permutations:
        for next_digit in range(list_digit[-1]+1, n_digits+1):
            initial_number = 9* (10**(next_digit-1))
            perm_list = permutations.setdefault(next_digit, [initial_number])
              
            for dig in list_digit:
                for item in permutations[dig]:
                    perm_list.append(initial_number + item)

            list_digit.append(next_digit)
    return permutations[n_digits]

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
