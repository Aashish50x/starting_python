lst=[1,2,3,4,5,6,7,8,9,0]
for i in lst:
    print(i)

for name in lst:
    print(name)

t=(1,2,3,4,5,6)  # tuple
for i in t:
    print(i)

# string 
a="Aashish"
for i in a:
    print(i)

for i in a:
    print(a)

# dictionary 
dic={1:"aashish",2:"abc",3:"asdf"}

for i in dic:
    print(dic)

for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key , value in dic.items():
    print(key,":", value)

for i in dic:
    print(i)

for i in dic.values():
    print(i)

for key in dic:
    print(key,":",dic[key])