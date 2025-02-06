# Write a program which finds out whether a given name 
# is present in a list or not

list=("aashish", "abc","xyz",'pqrs')

a=input("enter your username: ")

if (a in list):
    print("Username found in list.")
else:
    print("username not found in list.")