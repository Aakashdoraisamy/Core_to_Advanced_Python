l = [10,20,30,40,50,60]
l1 = int(input('enter Your input to remove:'))
for i in range(len(l)):
    if i == l1:
        del l[i]
        break
print(f'After removing {l1} the final list is:',l)