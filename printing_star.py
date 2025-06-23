# Write a program to print the following star pattern.

# for writing in this manner
# *

# *
# *

# *
# *
# * n==3

for i in range (1,4):
    for j in range (0,i):
        print("*")
    print("")


#  *
# ***
# ***** for n = 3

for i in range (1,4):
    for j in range (0,i):
        print("*", end="")
    print("")


# *** n=3
# **
# *

for i in range (0,4):
    for j in range (i,3):
        print("*", end="")
    print("")


#  *

# ***

# ***** for n = 3

for i in range (1,4):
    for j in range (0,i):
        print("*",end="")
    print("\n")






n=int(input("Enter no. of lines : "))
for i in range(0,n+1):
    for j in range(i,n+1):
        print(" "*(n-1),end="")
    print("*"*(2*i-1))