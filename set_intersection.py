set1 = {10,11,23,43,23}
set2 = {23,43,12,14,87,6}

print(set1.union(set2)) # prints union of set 1 and set 2
print(set1.intersection(set2)) # print common in set1 and set 2

set3={1,2,3,4,5}
set4={4,5,6,7,8}
print(set3-set4)  # delete common present in set4 from set3 and print left {1,2,3}
print(set4-set3)  # delete common present in set3 from set4 and print left {6,7,8}
# there is no order in set reprsentation


print(set3.union(set4)) # prints union of set 3 and set 4
print(set3.intersection(set4)) # print common in set3 and set 4
print(set4.intersection(set3)) # print common in set3 and set 4  both are same
print(set3.difference(set4)) # print different in set3 from set4
print(set4.difference(set3)) # print different in set4 from set3

set5={1,2,3,4,5,6,7,8,9,0}
# pop to retuen a rendom value from set 
print(set5.pop())
print(set5.pop())
print(set5)
print(set5.pop())
print(set5.pop())
print(set5.pop())
print(set5)

set6={1,23,1,5,65,76,23,756,86,3,57,5}
print("set is :",set6)
# pop to retuen a rendom value from set 
print('random pop:',set6.pop())
print('random pop:',set6.pop())
print('updted set is:',set6)
print('random pop:',set6.pop())
print('random pop:',set6.pop())
print('random pop:',set6.pop())
print('updted set is:',set6)