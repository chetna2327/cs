# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

# See PyCharm help at https://www.jetbrains.com/help/pycha

def fact(n):

    if(n==0 or n==1):
        return 1
    else:
        x=1
        while (n >1):
            x= x*n
            n-=1
        return x

n = int(input("enter the number:"))
print("factorial is:", fact(n))





