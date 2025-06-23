# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]

i=0
while(i<len(l)):
    if (l[i].startswith("S")):
        print("Hello ",l[i],"!")
    i+=1

for i in range(len(l)):
    if(l[i].startswith("H")):
        print("Hello",l[i],"!")
    i+=1

for name in l:
    if(name.startswith("R")):
        print("Hello",name,"!")
    i+=1