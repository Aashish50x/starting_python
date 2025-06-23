# reading txt file
#  for reading data from a file
f=open("file1.txt")  # nop need to define 'r' mode. its default
data = f.read()
print(data)
f.close()