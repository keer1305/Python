#we declare the datatype before, we can expand and shrink it
#we can add elements and find element using methods and index number of parti. value
#all values of same type

import array as arr
from array import *


val = array('i',[5,-7,6,4])

for i in range(4):
    print(val[i])

val.reverse()
print(val)

for i in range(len(val)):  #dynamic
    print(val[i])

for e in val:
    print(e)


#using characters:

val = array('u',['a','r','i'])
print(val)

val = array('i',[2,5,8,5,11,342,12])
newArray = array(val.typecode,(a*a for a in val))
print(newArray)

for i in newArray:
    print(i)

#using while:

i=0
while i<len(newArray):
    print(newArray[i])
    i+=1

