# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dic={}
a=input("Enter your name:")
b=input("Enter your favorite:")
dic.update({a:b})
a=input("Enter your name:")
b=input("Enter your favorite:")
dic.update({a:b})
a=input("Enter your name:")
b=input("Enter your favorite:")
dic.update({a:b})
a=input("Enter your name:")
b=input("Enter your favorite:")
dic.update({a:b})

print(dic)

# keys will update if same 
# it means if the name of two are same then it will update the dic and save last one 


# problem5.7
# If the names of 2 friends are same; what will happen to the program 
# in problem 5.6?

# keys will update if same 
# it means if the name of two are same then it will update the dic and save last one 

# problem5.8
# If languages of two friends are same; what will happen to the program 
# in problem 6?

# then it will show both the keys and values normaly