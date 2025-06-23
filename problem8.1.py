# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c


n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
n3=int(input("Enter num3 : "))

a=greatest(n1,n2,n3)
print(f"{a} is the greatest among all")


# you can do only this also . by this it print directly return value without putting it on variable.
# greatest(n1,n2,n3)
