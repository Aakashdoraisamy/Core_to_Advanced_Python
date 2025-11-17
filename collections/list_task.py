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


# WITHOUT USING INDEX METHOD

l = [10,20,30,40,50,60]
l1 = int(input('enter Your input to check the index:'))
index = -1
for i in range(len(l)):
    if l[i] == l1:
        index = i
        break
print(f'index of {l1} in list is {index} index place')
        
        
# WITHOUT USING REVERSE METHOD

l = [100,'Python','SQL','HTML','CSS',100]
new = []
for i in range(len(l)-1, -1, -1): # i = 5,4,3,2,1,0 it accesses the list in reverse order # taken input from last index value 5 and then stop until reach -1 because we need until zero and then to reverese we use -1 because deafult we use [::-1] for reverse
    new += [l[i]]
print(new)

# WITHOUT USING APPEND METHOD

l = [1, 2, 3, 4]
x = int(input("Enter element to append: "))
l += [x] 
print(l)

# WITHOUT USING EXTEND METHOD

l1 = [1, 2, 3]
l2 = [4, 5, 6]
for i in l2:
    l1 += [i]  
print(l1)

# WITHOUT USING INSERT METHOD

l = [10, 20, 30, 40]
p = int(input("Enter position to insert: "))
val = int(input("Enter value to insert: "))
l = l[:p] + [val] + l[p:]
print(l)

# WITHOUT USING COPY METHOD

l = [1, 2, 3, 4]
l_copy = [i for i in l]  
print(l_copy)

# WITHOUT USING CLEAR METHOD

l = [1, 2, 3, 4]
while len(l) > 0:
    del l[0]
print(l)

# WITHOUT USING SORT METHOD

l = [5, 1, 4, 2, 3]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)

# WITHOUT USING MAX METHOD

l = [5, 1, 7, 3]
max_val = l[0]
for i in l:
    if i > max_val:
        max_val = i
print(max_val)

# WITHOUT USING MIN METHOD

l = [5, 1, 7, 3]
min_val = l[0]
for i in l:
    if i < min_val:
        min_val = i
print(min_val)

