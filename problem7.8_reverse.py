# Write a program to print the following star pattern.
# * * *
# * * 
# *   for n = 3


n=int(input("Enter no. of lines = : "))

for i in range(0,n+1):
    print("*"*(n-i))