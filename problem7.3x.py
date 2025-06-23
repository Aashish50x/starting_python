# Attempt problem 1 using while loop. 

# Write a program to print multiplication table of a given number using for loop.

a=int(input("Enter a number: "))
print(f"Table of {a} is : ")

i=1
while(i<=10):
    print(f"{a} X {i} = {i*a}")
    i+=1