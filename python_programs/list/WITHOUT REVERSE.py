l = [100,'Python','SQL','HTML','CSS',100]
new = []
for i in range(len(l)-1, -1, -1): # i = 5,4,3,2,1,0 it accesses the list in reverse order # taken input from last index value 5 and then stop until reach -1 because we need until zero and then to reverese we use -1 because deafult we use [::-1] for reverse
    new += [l[i]]
print(new)
