# Write a program to greet a user with “Good day” using functions.


n=input("Enter your Name : ")

def greet(n):

    print(f"Hello {n}!\nHave a Good Day.")

# now calling function 
greet(n)

# another example 

n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
n3=int(input("Enter num3 : "))

def add(a,b,c):
    d=a+b+c
    print(f"Sum is {d}")
    return "Done" # this value goes to s

# calling function
s=add(n1,n2,n3)
print(s)


# method 2 

n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
n3=int(input("Enter num3 : "))

def add(a,b,c):
    d=a+b+c
    return sum  # this value goes to s

# calling function
s=add(n1,n2,n3)
print(f"Sum is {s}")
