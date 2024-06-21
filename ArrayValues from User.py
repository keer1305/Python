#ARRAY VALUES FROM USER:
from array import *

arr = array('i',[])
n=int(input("Enter the length of the array:"))

for i in range(n):
    x=int(input("enter the next value:"))
    arr.append(x)

print(arr)

#find the index of a value in array

n = int(input("Enter the value to search"))

k=0
for e in arr:
    if e==n:
        print(k)
        break
    k+=1

##using functions

print(arr.index(n))