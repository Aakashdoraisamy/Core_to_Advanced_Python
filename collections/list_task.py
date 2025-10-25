# WITHOUT USING COUNT METHOD

l = [1,2,3,4,5,12,43,90,87,1,2,5,9,8]
l1 = int(input("Enter a value to find the occurence: "))
count = 0
for i in l:
    if i == l1:
        count+=1
print(f"{l1} is found {count} times in the list")

# WITHOUT USING POP METHOD

l = [10,20,30,40,50,60]
# d = l[len(l)-1] # l[6-1] = 60
del l[len(l)-1]
print(f'After deleting the last element the final list:',l) 

# WIHOUT USING REMOVE METHOD

l = [10,20,30,40,50,60]
l1 = int(input('enter Your input to remove:'))
for i in range(len(l)):
    if i == l1:
        del l[i]
        break
print(f'After removing {l1} the final list is:',l)


# WITHOUT INDEX

l = [10,20,30,40,50,60]
l1 = int(input('enter Your input to check the index:'))
index = -1
for i in range(len(l)):
    if l[i] == l1:
        index = i
        break
print(f'index of {l1} in list is {index} index place')
        
        
# WITHOUT REVERSE 

l = [100,'Python','SQL','HTML','CSS',100]
new = []
for i in range(len(l)-1, -1, -1): # i = 5,4,3,2,1,0 it accesses the list in reverse order # taken input from last index value 5 and then stop until reach -1 because we need until zero and then to reverese we use -1 because deafult we use [::-1] for reverse
    new += [l[i]]
print(new)

