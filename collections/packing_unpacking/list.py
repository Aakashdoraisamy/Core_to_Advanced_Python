l = [0,0,7]
# for i in l:
#     print(i, end=' ')
    
l = [0,0,7]
print(*l)

a,b,c = l
print(a,b,c)

c,r,_7 = l
print(c,r,_7)

s = {0,0,7}
print(*s)
a,b,c = s
c,r,_7 = s
print(c,r,_7)