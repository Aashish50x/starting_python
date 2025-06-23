# Write a program to print the content of a list using while loops.

a=["aashish",12,"a123",23.44]

i=0
while (i<len(a)):
    print(a[i])
    i +=1



# using entering list variables from the user

b=input("Enter your list content : ")
a=[b]
c=input("Do you want to add more items  (y/n): ")
while True:
    if(c=="n"):
        break
    elif(c=="y"):
        b=input("Enter item : ")
        a.append(b)
        i+=1
        c=input("Do you want to add more items  (y/n): ")
    else:
        print("wrong option")
        break

for item in a:
    print("items of the list are :",a)

    
print(a)