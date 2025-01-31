# strings input is taken by simply input 
# strings are inmutal able . the main string will notchange it make another modified string
a = input("Enter the string: ")
print("String is : ",a)

# String  basic print function for writting specific index 
print("Printing specific index values: ")
name = "Aashish Kumar"
print("String is :", name)
# printing specific index 
print(name[1:5])  # from index 1 to 4
print(name[0:5])  # from index 0 to 4
print(name[0:2])  # from index 0 to 1
print(name[0:1])  # from index 0 to 1-1 , gives result only index 0, end index will not print

print(name[:1])  # print from starting to index 1-1
print(name[:5])  # print from starting to index 4

print(name[2:])  # print from index 2 to end
print(name[5:])  # print from index 5 to end