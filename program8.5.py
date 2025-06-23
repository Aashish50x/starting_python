# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *


def star(s):
    if s==0:
        print("")
    else:
        print("*"*s)
        star(s-1)

s=int(input("Enter natural number : "))
star(s)