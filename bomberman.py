#!/bin/python3

import math
import os
import random
import re
import sys
import copy

def bomberMan(n, grid):
    if ifPattenType2(grid):
        return bomberMan3(n, grid)
    else:
        return bomberMan1(n, grid)

def bomberMan1(n, grid):
    r = len(grid)
    c = len(grid[0])
    if n == 1:
        return grid
    if n == 2 or n == 4:
        return bomb_grid(r, c)
    grid = detonate(n, grid)
    if n == 3:
        return grid
    grid = detonate(n, grid)
    if n == 5:
        return grid
    n = n-5
    remaining_steps = n % 2
    if remaining_steps == 1:
        return bomb_grid(r, c)
    if remaining_steps == 0:
        return detonate(n, grid)

def bomberMan2(n, grid):
    r = len(grid)
    c = len(grid[0])
    if n == 1:
        return grid
    if n == 2 or n == 3 or n == 4:
        return bomb_grid(r, c)
    grid = detonate(n, grid)
    if n == 5:
        return grid
    n = n-5
    remaining_steps = n % 4
    if remaining_steps == 1 or remaining_steps == 2 or remaining_steps == 3:
        return bomb_grid(r, c)
    if remaining_steps == 0:
        return detonate(n, grid)

def bomberMan3(n, grid):
    r = len(grid)
    c = len(grid[0])
    remaining_steps = n % 4
    if remaining_steps == 1 or remaining_steps == 2 or remaining_steps == 3:
        return bomb_grid(r, c)
    if remaining_steps == 0:
        return detonate(n, grid)


def ifPattenType2(grid):
    return (''.join(grid)).find('O') == -1


def detonate(n, grid):
    r = len(grid)
    c = len(grid[0])
    oGrid = []
    for i in range(r):
        oGrid.append(['O']*c)
    for i in range(r):
        row_list = list((grid[i]))
        row = grid[i]
        j = row.find('O')
        while j != -1:
            oGrid[i][j] = '.'
            if i+1 < r:
                oGrid[i+1][j] = '.'
            if i-1 >= 0:
                oGrid[i-1][j] = '.'
            if (j+1) < c:
                oGrid[i][j+1] = '.'
            if (j-1) >= 0:
                oGrid[i][j-1] = '.'
            row_list[j] = '.'
            row = (''.join(row_list))
            j = row.find('O')
    for i in range(0, r):
        oGrid[i] = (''.join(oGrid[i]))
    return oGrid

def print_grid(grid):
    global fptr
    fptr.write('\n'.join(grid))
    fptr.write('\n')
    fptr.write('\n')

def bomb_grid(r, c):
    oGrid = []
    for i in range(r):
        oGrid.append(''.join(['O']*c))
    return oGrid

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item.rstrip())

    result = bomberMan(n, grid)
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
