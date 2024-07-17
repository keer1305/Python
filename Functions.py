def add(x,y):
    c = x +y
    print(c)

add(2,4)

def add_sub(a,b):
    c=a+b
    d=a-b
    print(c,d)

add_sub(100,9)

def add_sub1(a,b):
    c=a+b
    d=a-b
    return c,d

result1, res2 = add_sub1(4,7)
print(result1,res2)

def update(x):
    print("x id is", id(x))
    x=8
    print(id(x))
    print("x is" , x)

a=10
print("a id is" , id(a))
update(a)