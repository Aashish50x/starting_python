# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *


def star(s):
    for i in range (0,s+1):
        print("*"*(s-i))

s=int(input("Enter natural number : "))
star(s)