from numpy import*
def feb(x):
    a = 0
    b = 1
    if x<=0:
        print("invalid")
    elif x==1:
        print(a)
    elif x==2:
        print(a)
        print(b)

    else:
        for i in range(2,x):
            c = a+b
            a=b
            b=c
        print(c)
x= int(input("enter the range:"))
feb(x)

