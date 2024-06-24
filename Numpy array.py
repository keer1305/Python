from numpy import *

val = array([2,4,1,5,6])  #no need to mention type here for numpy

print(val)

#ways of creating array in numpy

arr = array([1,2,3,4,5.0])

print(arr.dtype)

arr = linspace(1,4,2) #spliting into 2 parts
print(arr)

arr=arange(1,15,2) #skips 2nd element
print(arr)

arr= logspace(1,40,5) #log base 10 to 1 ,log base 40 into 5 equal parts
print(arr)
print('%.2f' %arr[3])

arr = zeros(5,int)
print(arr)

arr = ones(5,float)
print(arr)

print(arr)

#Copying the array

arr = array([1,4,5,9])
arr1 = array([6,7,2,8])
print(sqrt(arr))
print(concatenate((arr,arr1)))

#multi dimensional array

arr3= array([[1,2,3,2,5,6],[4,5,6,4,7,5]])

print(arr3.ndim)
print(arr3.shape)
print(arr3.size)

#convert 2d array to 1d array
arr4=arr3.flatten()
print(arr4)

arr5 = arr4.reshape(3,4)
print(arr5)

arr5 = arr4.reshape(3,4)
print(arr5)