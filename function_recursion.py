# function recursion 
# finding factorial of given number

n1=int(input("Enter num1 : "))

def factorial(n1):
        if n1==0 or n1==1 :
            return 1
        else:
            return n1*factorial(n1-1)

print(f"factorial of {n1} is {factorial(n1)}")




# we can write this also
# no need to use else 

n1=int(input("Enter num1 : "))

def factorial(n1):
        if n1==0 or n1==1 :
            return 1
        return n1*factorial(n1-1)

print(f"factorial of {n1} is {factorial(n1)}")