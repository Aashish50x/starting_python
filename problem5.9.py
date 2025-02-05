# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# ans no 

s = {8, 7, 12, "Harry", [1,2]}
# a set cannot contain list or dic in it , it will show error because list and dic are mutualbe 
# and set doesnot contain mutuable data type 
# we cannot change in the index 
#  this will bw correct
s1 = {8, 7, 12}
print(s1)
# this will execute after removing line 5 from program