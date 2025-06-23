# readline function
# for reading single - single line 

f=open("file3.txt")
lines=f.readline()
print(lines)
lines=f.readline()
print(lines)
lines=f.readline()
print(lines)
print(type(lines))   # type of line is string

# readlines function
# for reading all lines / multiple lines in one command

f=open("file3.txt")
lines=f.readlines()
print(lines)
print(type(lines))  # type of line is list