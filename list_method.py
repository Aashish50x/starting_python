# methods in list 
a = ["aashish", "shivam", 5 , 'Rahul', 32.34 , True , '12', 'abc']
print(a)

a.append("girl")  # append "girl" new element at end
print(a)  # modified list (list has modified)
a.reverse()  # reverse the list
print(a)
a.insert(4,"Aa")  # insert 'Aa' at index 4
print(a)
a.remove("shivam")  # remove 'shivma' from list
print(a)
a.pop(6)  # remove index 6 element from list
print(a.pop(5))  # reomove index 5 fom list and also print it removed element
print(a)

b = [12,23,43,7,3,5,8,59,9,0,5,45,76,34,67,87]
print(b)

b.sort()  # sort the number list 
print(b)