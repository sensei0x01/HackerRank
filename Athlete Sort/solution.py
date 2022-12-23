# Python 3.x 

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #preper the input n,m, attribute values and K.
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # sort arr according to attribute in column k
    arr.sort(key=lambda l:l[k])

    # print(*map(lambda x: " ".join(x),list(map(lambda x: list(map(str,x)),arr))), sep='\n') #solution using map func

    # solution using nested loop
    for subArr in arr:
        for element in subArr:
            print(element,end=" ")
        print()
