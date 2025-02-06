# Write a program to find out whether a given
# post is talking about “Aashish” or not.
# applicable for both upper and lower case 


a=input("write your post : ")
b=a.lower()
if ("aashish" in b):
    print("This post is talking about Aashish.")
else:
    print("This post is not talking about Aashish.")


# short

a=input("write your post : ")
if ("Aashish".lower() in a.lower()):
    print("This post is talking about Aashish.")
else:
    print("This post is not talking about Aashish.")