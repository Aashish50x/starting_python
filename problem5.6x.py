# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dic={}
a=input("Enter your name:")
b=input("Enter your favorite:")
dic[a]=b
a=input("Enter your name:")
b=input("Enter your favorite:")
dic[a]=b
a=input("Enter your name:")
b=input("Enter your favorite:")
dic[a]=b
a=input("Enter your name:")
b=input("Enter your favorite:")
dic[a]=b

print(dic)

# keys will update if same 
# it means if the name of two are same then it will change the dic and save last one 