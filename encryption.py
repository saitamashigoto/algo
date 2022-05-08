#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    remove_space = s.replace(' ', '')
    length = len(remove_space)
    sqrt = math.sqrt(length)
    floor = math.floor(sqrt)
    ceil = math.ceil(sqrt)
    if ceil*floor < length:
        row = floor + 1
    else:
        row = floor
    column = ceil
    list_string = []
    i = 0
    result = dict()
    while i < length:
        j = 0
        while j < column and i + j < length:
            col_list = result.setdefault(j, [])
            col_list.append(remove_space[i+j])
            j += 1
        i += column   
    result_string = ''
    for list_char in result.values():
        result_string += (''.join(list_char) + ' ')
    return result_string.rstrip()



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input().rstrip()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
