# Write a program to find the greatest of four numbers entered by the user.

a1=int(input("Enter your 1st number: "))
a2=int(input("Enter your 2nd number: "))
a3=int(input("Enter your 3rd number: "))
a4=int(input("Enter your 4th number: "))

if (a1>a2):
    if(a1>a3):
        if(a1>a4):
            print(a1,"is greatest number.")
        else:
            print(a4,"is greatest number.")
    else:
        if(a3>a4):
            print(a3,"is greatest number.")
        else:
            print(a4,"is greatest number.")
else:
    if(a2>a3):
        if(a2>a4):
            print(a2,"is greatest number.")
        else:
            print(a4,"is greatest number.")
    else:
        if(a3>a4):
            print(a3,"is greatest number.")
        else:
            print(a4,"is greatest number.")
