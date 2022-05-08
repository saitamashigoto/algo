#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    len_G = len(G)
    len_P = len(P)
    i = 0
    k = 0
    prev_start_G = 0
    while i < len_G and k < len_P:
        start_G = G[i].find(P[k])
        i += 1
        if start_G != -1:
            if k == 0:
                prev_start_G = start_G
                k += 1
            elif k > 0 and prev_start_G == start_G:
                k += 1
            elif k > 0 and prev_start_G != start_G:
                k = 0
        else:
            k = 0
    if k == len_P:
        return 'YES'
    else:
        return 'NO' 
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item.rstrip())

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item.strip())

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
