d = {'a':12,'b':34,'c':45,'d':56}
remove_element = 'b'
if remove_element in d:
        del d[remove_element]
print(d)


d = {"a": 1, "b": 2, "c": 3}
last_key = ''
for key in d:  
    last_key = key
del d[last_key]
print(d)  

# 2nd way

d = {"a": 1, "b": 2, "c": 3}
c,l,k = 1,len(d),''
for i in d:
    if c == l:
        k = i
    c+=1
print(k,d[k])
del d[k]
print(d)

# 3rd way

d = {"a": 1, "b": 2, "c": 3}
l = [i for i in d]
last_key = l[-1]
print(last_key,d[last_key])
del d[last_key]
print(d)

#       (OR)

d = {"a": 1, "b": 2, "c": 3}
last_key = [i for i in d][-1]
print(last_key,d[last_key])
del d[last_key]
print(d)
