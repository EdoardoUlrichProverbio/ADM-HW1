####################################
#Python If-Else

import math
import os
import random
import re
import sys

def constraint(input_number):
    if input_number <= 0 or input_number > 100 :
        print("Numero non valido: inserire un numero compreso tra 1 e 100")
        return False
    else :
        comment(input_number)
        return input_number
    
def comment(input_number):
    if ( input_number in range (2,5) or input_number > 20 ) and input_number % 2 == 0 :
        print ("Not Weird")
    else :
        print ("Weird")

n = constraint(int(input()))

####################################################
#Arithmetic Operators
def constraint(input_number):
    if input_number <= 0 or input_number > 10**10 :
        print("Numero non valido: inserire un numero compreso tra 1 e 100")
        return False
    else :
        return input_number
    


a = constraint(int(input()))
b = constraint(int(input()))  

print( a + b)
print( a - b)
print( a * b)

####################################################
#Python: Division
a = int(input())
b = int(input())

print(a//b)
print (a/b)


####################################################
#Loops

def constraint(input_number):
    if input_number <= 0 or input_number > 20 :
        print("Numero non valido: inserire numero tra 1 e 20")
        return False
    else :
        return input_number

n = constraint(int(input()))

for i in range(n):
    print(i**2)

####################################################
#Write a function

def is_leap(year):
    leap = False

    if year % 4 == 0 :
        leap = True
        if year % 100 == 0 :
            leap = False
            if year % 400 == 0 :
                leap = True
   
    return leap


####################################################
# Print Function

n = int(input())
s = ""
for i in range(n) :
   s = s + str(i+1)

print(s)

####################################################
# List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())

my_list = [0,0,0]

final_list = []
for i in range(x+1):   
    for j in range(y+1) :
        for k in range(z+1):
            if i+j+k != n :               
                final_list.append ([i,j,k])
                            
print(final_list)

####################################################
# Find the Runner-Up Score!


n = int(input())
scores = list(set(map(int,input().strip().split(" "))))
scores.sort()
runner_up = scores[len(scores)-2]
print(runner_up)

####################################################
# Nested Lists

from operator import itemgetter
n = int(input())

my_list = [[] for i in range(n)]

for i in range(n):
    name = str(input())
    score = float(input())
    my_list [i].extend([name, score])

 
my_list.sort(key = itemgetter(1))
second_low_grade = 0
second_low_names = []

for i in range (n) :   
    if my_list[i-1][1] == my_list [0][1] and my_list[i][1] != my_list [0][1]:
        second_low_grade  =  my_list[i][1]

for i in range (n) :  
    if my_list [i][1] == second_low_grade:
        second_low_names.append (my_list[i][0])
 
second_low_names.sort()

print(*second_low_names, sep = "\n") 

####################################################
# Finding the percentage


n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average = sum(student_marks[query_name])/3
print("%.2f"%(average))

####################################################
# Tuples

n = int(input())

list1 = tuple((map(int,input().split(" "))))

print(hash(list1))



####################################################
# sWAP cASE
def swap_case(s):
    return s.swapcase()
    


####################################################
# String Split and Join
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


####################################################
# What's Your Name?
def print_full_name(a, b):
    c = a + " " + b
    print("Hello " + c + "! You just delved into python.")
    

####################################################
# Mutations
def mutate_string(string, position, character):
    letter = list(string)
    letter [position] = character
    string = "".join(letter)
    return string


####################################################
# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count = count + 1
    return count


####################################################
# String Validators
s = input()
print ( any(c.isalnum() for c in s) )
print ( any(c.isalpha() for c in s) )
print ( any(c.isdigit() for c in s) )
print ( any(c.islower() for c in s) )
print ( any(c.isupper() for c in s) )


####################################################
# Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


####################################################
# Text Wrap

def wrap(string, max_width):

    wrapper = textwrap.TextWrapper(max_width) 
    word_list = wrapper.wrap(string)     
    result = ""
    for element in word_list :       
        result = result  + element + "\n"
    return result

####################################################
# Designer Door Mat

N,M = map(int,input().split(" "))


c = ".|."
k = int((M-3)/2)
half = int((N-1)/2)

for i in range((half)):
    print((c*i).rjust(k , '-' )+c+(c*i).ljust(k , '-' ))

print('WELCOME'.center(M,'-'))

for i in reversed(range((half))):
    print((c*i).rjust(k , '-' )+c+(c*i).ljust(k , '-' ))


####################################################
# String Formatting

def print_formatted(number):
    n = number
    results = []
    for i in range(1, n+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexa = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])
        results.append([decimal, octal, hexa, binary])
        width = len(results[-1][3])
    for i in results:
        print(*(rep.rjust(width) for rep in i))


####################################################
# Alphabet Rangoli

import string

def print_rangoli(size):
    # your code goes here
    alpha = list(string.ascii_lowercase)
    my_string = alpha [0:size]

    for i in range(size-1, -size, -1):
        x = abs(i)
        line = my_string[size:x:-1]+my_string[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)
       

####################################################
# Capitalize!

import string

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
      s = s.replace(x, x.capitalize())
    return s      

####################################################
# The Minion Game
def minion_game(s):
   
    vowels = 'aeiouAEIOU'

    kevin_score = 0 
    stuart_score = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score  += (len(s)-i)
        else:
            stuart_score += (len(s)-i)

    if kevin_score > stuart_score:
        print ("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print ("Stuart", stuart_score)
    else:
        print ("Draw")


####################################################
# Merge the Tools!
def merge_the_tools(string, k):
    for x in range(0,len(string), k):

        res = string[x:x+k]
        new = ""
        for i in res:
            if i not in new:
                new = new + i
        print(new)


####################################################
# The Captain's Room

d=input()   
a=input().split()  

s1=set() 
s2=set() 


for i in a:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)

s3=s1.difference(s2)
print (list(s3)[0])


####################################################
# Check Subset
T= int(input())

for _ in range(T):

    Atot = int(input())
    A = set(input().split())


    Btot = int(input())
    B = set(input().split())

    C = B.difference(A)

####################################################
# Introduction to Sets
def average(array):
    total = 0
    set1 = list(set(array))
    for x in set1:
        total += x
    
    avg = float(total/(len(set1)))    
    
    return avg


####################################################
# Symmetric Difference
n1,arr1 = int(input()), set(map(int, input().split()))
n2,arr2 = int(input()), set(map(int, input().split()))

diff1 = arr1.difference(arr2) 
diff2 = arr2.difference(arr1) 

sim = sorted(diff1.union(diff2), key= int)
for x in sim:
    print(x )



####################################################
# No Idea!
nm, arr = list(map(int, input().split())), list(map(int, input().split()))
n, m = set(map(int, input().split())), set(map(int, input().split()))
happyness = 0
for x in arr :
    if x  in n :
        happyness += 1
    
    if x  in m :
        happyness += -1
print(happyness)


####################################################
# Set .add()

n = int(input())
country = set()
for _ in range(n):
    country.add(input())

print (len(country))


####################################################
# Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())) :

    command =input().split()

    if command[0]== "pop" :
        s.pop()
    if command[0]== "remove" :
        s.remove(int(command[1]))
    if command[0]=="discard" :
        s.discard(int(command[1]))

print (sum(s))

####################################################
# Set .union() Operation
N, Na = int(input()), set(map(int, input().split()))
B, Ba = int(input()), set(map(int, input().split()))

print(len(Na.union(Ba)))


####################################################
# Set .intersection() Operation
N, Na = int(input()), set(map(int, input().split()))
B, Ba = int(input()), set(map(int, input().split()))

print(len(Na.intersection(Ba)))


####################################################
# Set .difference() Operation
N, Na = int(input()), set(map(int, input().split()))
B, Ba = int(input()), set(map(int, input().split()))

print(len(Na.difference(Ba)))



####################################################
# Set .symmetric_difference() Operation
N, Na = int(input()), set(map(int, input().split()))
B, Ba = int(input()), set(map(int, input().split()))

print(len(Na^(Ba)))


####################################################
# Set Mutations
N, NA = int(input()), set(map(int, input().split()))

for _ in range(int(input())):

    command =input().split()
    B = set(map(int, input().split()))

    getattr(NA, command[0])(B)   


print(sum(NA))    


####################################################
# Check Strict Superset
A = set(map(int, input().split()))
q, N = 0, int(input())
for _ in range(N):

    B = set(map(int, input().split()))
    if A.issuperset(B) :
        q += 1
  
if q == N :
    result = True
else :
    result = False

print(result)


####################################################
# Calendar Module
import calendar

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
data = list(map(int, input().split()))
a = calendar.weekday(data[2], data[0], data[1])
print (week_days[a].upper())


####################################################
# Time Delta

import math
import os
import random
import re
import sys

from datetime import datetime

def time_delta(t1, t2):
    
    f= '%a %d %b %Y %X %z'
    t1 = datetime.strptime(t1, f) 
    t2 = datetime.strptime(t2, f) 
    diff = (t2-t1).total_seconds()  
    return abs(int(diff))

t = int(input())
for _ in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)


####################################################
# Exceptions
n = int(input ())

for i in range(n):
    d = list(input().split())
 
    try :
        print(int(d[0])//int(d[1])) 
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    
    except ValueError as e:
        print ("Error Code:",e)


####################################################
# collections.Counter()


N_size = int(input())
size = list(map(int,input().split()))
customers = int(input())
total = 0
for _ in range(customers) :
    a = list(map(int,input().split()))
    if a[0] in size :
        total += a[1]
        size.remove(a[0])
print (total)

####################################################
# DefaultDict Tutorial

from collections import defaultdict

n,m = list(map(int,input().split()))
A = defaultdict(list)

for i in range(1 , n+1):
    A[input()].append(i)
for i in range(m):
    print(*A[input()] or [-1])

####################################################
# Collections.namedtuple()
from collections import namedtuple

n, H , total = int(input()), input(), 0

Records = namedtuple('Records', H)

for i in range (n):
     record = Records(*input().split())
     total += int(record.MARKS)

print (round((total/n),2))


####################################################
# Collections.OrderedDict()
from collections import OrderedDict
o_d = OrderedDict()
for i in range (int( input())):
    data= input().split()
    order = " ".join(data[0: len(data)-1])
    price = int(data[len(data)-1])
    if order not in o_d:
        o_d[order] = int(price)
    else:
        o_d[order] +=int(price)

for item in o_d:
    print(item, o_d[item]) 

####################################################
# Word Order
from collections import OrderedDict
O_D = OrderedDict()
for _ in range (int(input())):
    word = input()

    if word not in O_D:
        O_D[word] = 1
    else:
        O_D[word] += 1
print(len(O_D))
for x in O_D:
    print(O_D[x], end= ' ') 

####################################################
# Collections.deque()
from collections import deque

d= deque()

for _ in range (int(input())):
    
    command =input().split()
    if len(command) == 2:
        getattr(d, command[0])(command[1])   
    else :
         getattr(d, command[0])()

print (*d)


####################################################
# Piling Up!
from collections import deque
n = int(input())
for _ in range (n):
    k = int(input())
    d=list(map(int,input().split()))
    if(d[0]==max(d) or d[k-1]==max(d)):print("Yes")
    else: print("No")


####################################################
# Zipped!

nm= list(input().split())
marks = nm[0]
stud = int(nm[1])
S_m = []
for i in range(stud):
    S_m.append( list(map(float, input().split())))

#print(tuple(zip(*S_m)))

for personal_score in zip(*S_m):
    print (sum(personal_score)/len(personal_score))

####################################################
# Athlete Sort

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
    arr.sort(key=lambda a: a[k]) 
    for i in range(n):
        print(*arr[i])

####################################################
# Map and Lambda Function

cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])

####################################################
# Arrays

def arrays(arr):
    return numpy.array(arr, float)[::-1]


####################################################
# Shape and Reshape
import numpy

A= numpy.array(input().split(" "),int)
print (numpy.reshape(A,(3,3)))      


####################################################
# Concatenate
import numpy as ny

N, M, P = map(int,input().split())
array_N=[]
array_M=[]
for i in range(N):
    line = list(map(int,input().split()))
    array_N.append(line)

for i in range(M):
    line = list(map(int,input().split()))
    array_M.append(line)


array_N = ny.array(array_N).reshape(N,P)
array_M = ny.array(array_M).reshape(M,P)

print(ny.concatenate((array_N, array_M), axis = 0))


####################################################
# Zeros and Ones

import numpy
a = list(map(int,input().split()))
print (numpy.zeros(a,dtype = numpy.int))  
print (numpy.ones(a,dtype = numpy.int))

