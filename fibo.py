#!/bin/python3

import math
import os
import random
import re
import sys

fibo = {0: 0, 1: 1}
fibo_list = [0, 1]

def isFibo(n):
    return calculateFibo(n)

def calculateFibo(n):
    global fibo, fibo_list
    if n in fibo:
        return 'IsFibo'
    else:
        last_element = fibo_list[-1]
        if n < last_element:
            return 'IsNotFibo'
        while True:
            next_number = fibo_list[-1] + fibo_list[-2]
            fibo_list.append(next_number)
            fibo[next_number] = next_number
            if n == next_number:
                return 'IsFibo'
            elif next_number > n:
                return 'IsNotFibo'

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
