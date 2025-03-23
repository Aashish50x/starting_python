# print 1 to 100 but the value will be 50 then break 

for i in range(1,101):   # for 1 to 100
    if (i==50):
        break  # exit the loop
    print(i)

# print 1 to 100 but the value will be 50 then not break skip that condition loop / iteration
for i in range(1,101):   # for 1 to 100
    if(i==50):
        continue  # skip this iteration
    print(i)