#!/bin/python3

import math
import os
import random
import re
import sys

memo = dict()

def buildDict(k, s):
    # Write your code here
    sign = tuple(s)
    if sign in memo:
        return
    memo[sign] = doesSaisfyCriteria(k, s)
    length = len(s)
    if length <= 2:
        return
    for i in range(length):
        new_set = s[0:i] + s[i+1:]
        buildDict(k, new_set)
        
def nonDivisibleSubset(k, s):
    buildDict(k, s)
    sorted_list = []
    for key in memo:
        if memo[key]:
            sorted_list.append(key)
    sorted_list.sort(key=len, reverse=True)
    if len(sorted_list) == 0:
        return 0
    return len(sorted_list[0])

def doesSaisfyCriteria(k, s):
    if k == 1:
        return True
    
    length = len(s)
    
    if length == 1:
        return True
    
    for i in range(length-1):
        for j in range(i+1, length):  
            if (s[i] + s[j]) % k == 0:
                return False
    return True

    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))
    
    s.sort()

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
