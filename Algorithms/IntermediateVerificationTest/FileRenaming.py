import math
import os
import random
import re
import sys



#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

def renameFile(newName, oldName):
	# 沒想到解法
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    newName = input()

    oldName = input()

    result = renameFile(newName, oldName)

    fptr.write(str(result) + '\n')

    fptr.close()
