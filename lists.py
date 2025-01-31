# lists are mutualable it means it can be changes after defining
# list can be change but string cannot be change

list = ['Apple',12,"Mango", 12.435 , 11 , True , False ]
# list can store multiple data types in one 

print(list[0])  #print apple
print(list[3])  #print 12.435

# modifing index 0
list[0] = "Car"
print(list[0])
print(list)  #modified list

# print length of strong
print(len(list))

# printing specific index 
print(list[1:5])  # from index 1 to 4
print(list[0:5])  # from index 0 to 4
print(list[0:2])  # from index 0 to 1
print(list[0:1])  # from index 0 to 1-1 , gives result only index 0, end index will not print

print(list[:1])  # print from starting to index 1-1
print(list[:5])  # print from starting to index 4

print(list[2:])  # print from index 2 to end
print(list[5:])  # print from index 5 to end


# Counting in list
print(list.count("a"))  # 3 (counts occurrences of "a" as list element)
print(list.count(12))  # 3 (counts occurrences of "a" as list element)
