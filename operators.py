# Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)
print("")

# Assignment Operators
a = 4 - 2  # Assign 4-2 in a
print(a)
b = 6
b += 3  # Increment the value of b by 3 and then assign it to b
print(b)
d = 6
d *= 3  # multiply the value of c by 3 and then assign it to c
print(d)
print("")

# comparison operator
print("comparison operators")
# return value of comparison operator is always boolean
e=5>4
print(e)  # give true/false
f=5>6
print(f)
print("")

# logical operators
print("logical operators")
# truth table of 'or'
print("truth table of OR")
g1= True or False # give output true
g2= True or True # give output true
g3= False or False # give output false
g4= False or True # give output true

print('true or false is ',g1)
print('true or true is ',g2)
print("false or false is ",g3)
print("false or true is ",g4)
print("")
# truth table of 'and'
h1= True and False # give output false
h2= True and True # give output true
h3= False and False # give output false
h4= False and True # give output false
print("truth table of AND")
print('true and false is ',h1)
print('true and true is ',h2)
print("false and false is ",h3)
print("false and true is ",h4)
print('')

print(not(False)) # not will convert false to true
print(not(True)) # not will convert true to false
