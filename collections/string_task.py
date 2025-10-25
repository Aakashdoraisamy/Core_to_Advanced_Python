# # s = input("Enter a string: ")
# # new_s = ""
# # for c in s:
# #     if 'A' <= c <= 'Z':
# #         new_s += chr(ord(c) + 32)
# #     elif 'a' <= c <= 'z':
# #         new_s += chr(ord(c) - 32)
# #     else:  
# #         new_s += c
# # print("Converted string:", new_s)

# # assignmet update the values without using build in methods and for set default also
# # assignmet upper character without build in method for isupper also


d = {'name':['Batman','Captain America'],'Marks':[99,99]}
new_key = 'city'
new_value = ['Gotham','New York']
d[new_key] = new_value
# if new_key not in d:
#     d[new_key] = new_value
print(d)

d = {'name':['Batman','Captain America'],'Marks':[99,99]}
new_key = 'name'
new_value = ['Batman','Captain America','Spiderman']
if new_key not in d:
    d[new_key] = new_value
print(d)

s = input("Enter a string: ")
new_s = "" 
for c in s:
    if c>= 'a' and c <= 'z': 
        new_s += chr(ord(c) - 32)
print(new_s)

s = input("Enter a string: ")
is_upper = True
# is_lower = False
c1=0
for c in s:
    # if c>= 'a' and c <= 'z': 
    #     # print(is_upper)
    #     is_upper = False
    #     break
    if 'A'<=c<='Z':
        c1+=1
    # else:
    #     print(is_lower)
    #     break
if c1==len(s):
    print('It is Upper case')
else:
    print('It is Lower')
