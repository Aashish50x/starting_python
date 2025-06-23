# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is greatest in all three.")
        else:
            print(f"{c} is greatest in all three.")
    else:
        if b>c:
            print(f"{b} is greatest in all three.")
        else:
            print(f"{c} is greatest in all three.")


n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
n3=int(input("Enter num3 : "))

greatest(n1,n2,n3)