#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#

def movingTiles(l, s1, s2, queries):
    result = list()
    for q in queries:
        if s1 < s2:
            x = (s1 * math.sqrt(2) * (l - math.sqrt(q))) / (s2 - s1)
            x /= s1
        else:
            x = (s2 * math.sqrt(2) * (l - math.sqrt(q))) / (s1 - s2)
            x /= s2
        x = '%f' % x
        result.append(x)
    return result

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
