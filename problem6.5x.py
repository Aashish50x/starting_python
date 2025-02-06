# Write a program which finds out whether a given name 
# is present in a list or not
# list data is also taken from user 

l=[]
s=int(input("enter your number of username in list: "))

i=0
while(i<s):
    a=input("enter your list usernames: ")
    l.append(a)
    i+=1


b=input("enter your username to be search : ")

if (b in l):
    print("Username found in list.")
else:
    print("username not found in list.")