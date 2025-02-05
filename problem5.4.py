# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(s)
print(len(s))
# it returns len 2 because in python 1==1.0 it gives true because pythons compares
# the value not data type that it is int or float 
# this is python behaviour