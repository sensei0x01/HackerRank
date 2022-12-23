

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda l:l[k])
    # print(*map(lambda x: " ".join(x),list(map(lambda x: list(map(str,x)),arr))), sep='\n')
    for subArr in arr:
        for element in subArr:
            print(element,end=" ")
        print()
