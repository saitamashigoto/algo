#!/bin/python3

import math
import os
import random
import re
import sys


def solve(c):
    p = 10**9 + 7
    c_dict = {}
    for i in c:
        v = c_dict.setdefault(i, 0)
        c_dict[i] = v + 1
    sorted_numbers = list(c_dict.keys())
    sorted_numbers.sort()
    res = 1
    picked_up = 0
    pickable = pickableCards(c_dict, sorted_numbers, picked_up)    
    while (pickable-picked_up) > 0 and picked_up < len(c):
        res = (res * (pickable-picked_up)) % p
        picked_up += 1
        pickable = pickableCards(c_dict, sorted_numbers, picked_up)
    if picked_up < len(c):
        return 0
    return res

def solve2(c):
    p = 10**9 + 7
    c_dict = {}
    for i in c:
        v = c_dict.setdefault(i, 0)
        c_dict[i] = v + 1
    if not 0 in c_dict:
        return 0
    sorted_numbers = list(c_dict.keys())
    sorted_numbers.sort()
    return cumulativeCards(c_dict, sorted_numbers, p, c)


def cumulativeCards(c_dict, sorted_numbers, p, c):
    i = 0
    picked_up = 0
    pickable_cards = c_dict[0]
    res = 1
    while True:
        if (i < len(sorted_numbers) - 1) and sorted_numbers[i+1] <= picked_up:
            pickable_cards += c_dict[sorted_numbers[i+1]]
            i += 1
        if pickable_cards <= 0:
            break
        res  = (res * pickable_cards) % p
        picked_up += 1
        pickable_cards -= 1
    
    return res if len(c) == picked_up + pickable_cards else 0


def pickableCards(c_cards, sorted_cards, picked_up):
    res = 0
    for i in sorted_cards:
        if i > picked_up:
            break
        res += c_cards[i]
    return res


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        c_count = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        result = solve2(c)

        fptr.write(str(result) + '\n')

    fptr.close()
