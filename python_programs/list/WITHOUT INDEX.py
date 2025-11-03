l = [10,20,30,40,50,60]
l1 = int(input('enter Your input to check the index:'))
index = -1
for i in range(len(l)):
    if l[i] == l1:
        index = i
        break
print(f'index of {l1} in list is {index} index place')