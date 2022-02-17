#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#

def getCurrentMaxArea(widthSeperatorList, heightSeperatorList):

    startPos = 0
    widthList = []
    widthSeperatorList.sort()
    for endPos in widthSeperatorList:
        widthList.append(endPos - startPos)
        startPos = endPos

    startPos = 0
    heightList = []
    heightSeperatorList.sort()
    for endPos in heightSeperatorList:
        heightList.append(endPos - startPos)
        startPos = endPos

    return max(widthList) * max(heightList)


def getMaxArea(w, h, isVertical, distance):
    # Write your code here
    widthSeperatorList = [w]
    heightSeperatorList = [h]
    result = []
    for isV, d in zip(isVertical, distance):
        if isV:
            if d > w or d < 0:
                continue
            widthSeperatorList.append(d)
        else:
            if d > h or d < 0:
                continue
            heightSeperatorList.append(d)
        result.append(getCurrentMaxArea(
            widthSeperatorList, heightSeperatorList))
    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w = int(input().strip())

    h = int(input().strip())

    isVertical_count = int(input().strip())

    isVertical = []

    for _ in range(isVertical_count):
        isVertical_item = int(input().strip()) != 0
        isVertical.append(isVertical_item)

    distance_count = int(input().strip())

    distance = []

    for _ in range(distance_count):
        distance_item = int(input().strip())
        distance.append(distance_item)

    result = getMaxArea(w, h, isVertical, distance)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
