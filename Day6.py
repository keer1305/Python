#if elif #nested if
#if a number is odd or even
x=6
r = x % 2

if r==0:
    print("Even")
    if x>5:
        print("great")
    else:
        print("not so great")
else:
    print("odd")
print("bye")

#if elif else

# x = int(input("enter the number: "))
#
# if x==1:
#     print("one")
# elif x==2:
#     print('two')
# elif x==4:
#     print('four')
# else:
#     print('wrong input')


#WHILE LOOP

# i=1
# while i<=5:
#     print("keer")
#     i=i+1

# i=1
# while i<=5:
#     print("keer",end=" ") #need space between keer and rock
#     j=1
#     while j<=4:
#         print("rocks",end=" ")
#         j=j+1
#     i=i+1
#     print() #to print keer in new line


###FOR LOOPS

# x=['KEER',23,5.4]
#
# for i in x:
#     print(i)
#
# x = 'keerthu'
# for i in x:
#     print(i)

# for i in range(10):
#     print(i)
#
# for i in range(2,12,1):
#     print(i)
# for i in range(21,12,-1):
#     print(i)

# for i in range(1,21):  #printing without 5 divisibles
#     if i%5!=0:
#         print(i)

####  BREAK #######
# av=10 #available qty is 10
# x = int(input("how many candy you want: "))
# i=1
# while i<=x:
#     if i>av:
#         print("out of order")
#         break
#     print("candy")
#     i=i+1
#
# print("goodbye")

### CONTINUE ####
#print all values from 1 to 100 which are not divisible by 3

# for i in range(1,101):
#     if i%3 ==0 or i%5 ==0:
#         continue
#
#     print(i)
#
# print("bye")

### PASS ###

# for i in range(1,101):
#     if (i%2 != 0):
#         pass
#
#     else:
#         print(i)

### BREAK VS CONTINUE VS PASS

for i in range(5):
    if i==3:
        break
    print("hello ", i)

def fun():  #to keep function empty we use pass
    pass

