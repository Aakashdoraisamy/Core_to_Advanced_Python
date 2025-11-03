l = [10,10,20,30,20,10,10,10]

s = set(l)

l1 = list(s)

print(l1)




l = [10,10,20,30,20,10,10,10]

l1 = []

for x in l:

    if x not in l1:

        l1.append(x)

print(l1)