#!/bin/python3

import math
import os
import random
import re
import sys


def factors(n):
    fact1 = []
    fact2 = []
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            fact1.append(i)
            if n // i != i:
                fact2.append(n // i)
        i += 1
    return fact1 + fact2[::-1] + [n]

def s(st):
    list_digit = list()
    list_digit[0:] = str(st)
    for i in range(len(list_digit)):
        list_digit[i] = int(list_digit[i])
    return sum(list_digit)


def solve(n):    
    facts = factors(n)
    dts = {}
    for i in range(len(facts)):
        sm = s(facts[i])
        dts.setdefault(sm, []).append(facts[i])
    list_sm = list(dts.keys())
    list_sm.sort()
    list_fact = dts[list_sm[-1]]
    list_fact.sort()
    print(list_fact[0])


if __name__ == '__main__':
    n = int(input().strip())
    solve(n)
