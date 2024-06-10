#print numbers only divisible by 5

num = [12,24,2252,152,26]

for i in num:
    if i % 5 ==0:
        print(i)
        break
else:
    (print("not found"))


##PRIME NUMBERS

n = 10

for i in range(2,n):
    if n%i ==0:
        print("not prime")
        break

    else:
        print("Its a prime number")
        break