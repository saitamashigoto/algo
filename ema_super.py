#!/bin/python3

import math
import os
import random
import re
import sys


def twoPluses(grid):
    pluses = dict()
    r = len(grid) 
    c = len(grid[0])
    findPlusRow(r//2, c//2, grid, pluses)
    area_key_list = list(pluses.keys())
    area_key_list.sort(reverse=True)
    area_key_list_length = len(area_key_list)
    max_area_list = []
    # print(pluses)
    for i in range(area_key_list_length):
        area_row = area_key_list[i]
        area_row_point_list = pluses[area_row]
        area_row_point_list_len = len(area_row_point_list)
        for j in range(area_key_list_length):
            area_column = area_key_list[j]
            for k in range(area_row_point_list_len):
                point1 = area_row_point_list[k]
                result_area = calculatePlusArea(point1, area_row, pluses, area_column)
                if result_area:
                    max_area_list.append(result_area)
                    break
    max_area_list.sort(reverse=True)
    return max_area_list[0]


def calculatePlusArea(point1, src_len, area_dict, tar_len):
    area_list = area_dict[tar_len]
    area_point1 = (src_len * 2)-1
    area_point2 = (tar_len * 2)-1
    
    for i in range(0, len(area_list)):
        result_over = doPlusOverlap(point1, src_len, area_list[i], tar_len)
        # print(point1, area_list[i], src_len, tar_len, result_over)
        if not result_over:
            return area_point1 * area_point2
    return False

def doPlusOverlap(point1, len1, point2, len2):
    if len1 == len2 and point1 == point2:
        return True
    set1 = calculatePlusPoints(point1, len1)
    set2 = calculatePlusPoints(point2, len2)
    # print(point1, point2, len1, len2, set1, set2, set1.intersection(set2))
    return len(set1.intersection(set2)) > 0

def calculatePlusPoints(point, length):
    enlarge = (length-1)/2
    set1 = set()
    set1.add(point)
    i = 1
    while i <= enlarge:
        set1.add((point[0]-i, point[1])) 
        set1.add((point[0]+i, point[1])) 
        set1.add((point[0], point[1]-i)) 
        set1.add((point[0], point[1]+i)) 
        i += 1
    return set1

def findPlusRow(x, y, grid, pluses):
    r = len(grid)
    if x >= r or x < 0:
        return pluses
    findPlusColumn(x, y, grid, pluses)
    i = 1
    while (x+i) < r:
        findPlusColumn(x+i, y, grid, pluses)
        i += 1
    i = 1
    while(x-i) >=0:
        findPlusColumn(x-i, y, grid, pluses)
        i += 1
        

def findPlusColumn(r, y, grid, pluses):
    c = len(grid[0])
    if y >= c or y < 0:
        return pluses
    plus = maxPlusLength(r, y, grid)
    if plus > 0:
        pluses_dict = pluses.setdefault(plus, [])
        pluses_dict.append((r, y))
    i = 1
    while (y+i) < c:
        plus = maxPlusLength(r, y+i, grid)
        if plus > 0:
            pluses_dict = pluses.setdefault(plus, [])
            pluses_dict.append((r, y+i))
        i += 1
    i = 1
    while (y-i) >=0:    
        plus = maxPlusLength(r, y-i, grid)
        if plus > 0:
            pluses_dict = pluses.setdefault(plus, [])
            pluses_dict.append((r, y-i))
        i += 1

def maxPlusLength(x, y, grid):
    r = len(grid)
    c = len(grid[0])
    if grid[x][y] != 'G':
        return -1
    plusLength = 1
    i = 1
    while (x+i) < r and (x-i) >=0 and (y+i) < c and (y-i) >=0:
        if grid[x+i][y] != 'G':
            break
        if grid[x-i][y] != 'G':
            break
        if grid[x][y-i] != 'G':
            break
        if grid[x][y+i] != 'G':
            break
        i += 1
    result = plusLength + ((i-1)*2)
    # print(x, y, result)
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
