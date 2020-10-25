#########################################################
#1 Birthday Cake Candles
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

##########################################################
#2 Number Line Jumps

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v2== v1: return "NO"
    a = (x2-x1)%(v1-v2)
    if v2 >= v1  or a!=0:  return "NO"
    elif a==0:  return "YES"
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

##########################################################
#3  Viral Advertising

import math
import os
import random
import re
import sys

def viralAdvertising(n):

    a, sum = 5, 0    
    for _ in range (n):
        sum += a//2
        a = (a//2)*3
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

###########################################################
#4 Recursive Digit Sum 

import math
import os
import random
import re
import sys

def superDigit(n, k):
    super_n=0
    if len(n) == 1:
        return int(n)
    for x in n:
        super_n += int(x) * k
    return superDigit(str(super_n), 1) 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n,k)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()


###########################################################
#5 Insertion Sort - Part 1

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):

   for i in reversed(range (n)):
        x = arr[i]
        y = i
        while y > 0 and arr[y-1] > x :
            arr[y] = arr[y-1]
            y = y-1
            arr[y] = x
            print (*arr)       
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)


###########################################################
#6 Insertion Sort - Part 2

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
   for i in range(n-1):       
        while i >= 0 and arr[i+1] < arr[i] :
            x= arr[i+1]
            arr[i+1]= arr[i]
            arr[i]=x
            i+= -1
        print(*arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)


