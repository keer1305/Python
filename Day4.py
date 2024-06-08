#Varaible address
num=5
print(id(num))

name = 'keer'
print(id(name))

a=10
b=a
print(a)

print(id(a))
print(id(b))
print(id(10))

#Datatypes in python

#SWAP 2 VARIABLES IN PYTHON

a=5
b=6

temp = a #save the a value in temp variable to assign it to b later
a = b  #saving b value to a
b = temp  #saving temp 5 value to b

print(a)
print(b)

#swapping without 3rd variable

a=5
b=6

a=a+b
b=a-b #5
a=a-b #6
print("without temp" ,a)
print(b)

#using XOR
a=11
b=20

a=a^b
print(a)
b=a^b
a=a^b
print("using XOR" ,a)
print(b)

print(f"a={a},b={b}") # Using f-string
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."

#Using format() Method
greeting1 = "Hello, my name is %s and I am %d years old." % (name, age)
#Using % Operator
greeting2 = "Hello, my name is {} and I am {} years old.".format(name, age)

print(greeting,greeting1,greeting2)
print("greeting\ngreeting1\ngreeting2")