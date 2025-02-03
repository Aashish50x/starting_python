# dictionary data type 
a = {"aashish": 23 , "abs":34,"qwe":"xyz", 32 : "AA", 43 : 12, list : [1,2,3,4,5]}
print(a)
d={}   # empty dict.

# to print type of the varaible
print(type(a))

# # to print variable and type both
print(a,type(a))

# # to print the lenght of the dictionary
print(len(a))
print(a.keys())
print(a.values())
b= a.items()
print(b)
print(a["aashish"])   # gives error if not present
# to get 
print(a.get("abs"))   # gives none if not present

# to update dic 
a.update({"aashish": 99})
a.update({"a": 99})
a.update({"aashish": "100"})
print(a)

# to set value or change
print(a.setdefault("d", 4))  # Adds 'd': 4 if not present
print(a)
print(a.setdefault("abs", 4))
print(a)

# gives the value of key or return the value of key 
# a.pop("aashish") 
print(a.pop("aashish"))
# to remove last item from the dic 
print(a.popitem())

c=a.copy()
print(c)

# to clear dic 
c.clear()
print(c)
