# sets are unordered and cannot call by indexing and cannot be changed

s = {10,'aashish',19,13.34,14,14,14,13,13}  # set doesn't repeate in printing
print(s)
empty_set = set() # don't use set={} it will create a empty dictionary
print(type(s))
print(s,type(s))


# add 
s.add(55)
print(s)

# to copy
a=s.copy()
print(a)

# to clear
a.clear()   # became a empty set
print(a)

print(set())

# len of set 
print(len(s))
# to remove specific from the set 
s.remove(14)
print(s)

# pop removes random form the set 
s.pop()
print(s)

# to add
s.add(10)
print(s)