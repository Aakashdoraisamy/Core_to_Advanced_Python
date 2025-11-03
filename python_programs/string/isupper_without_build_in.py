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