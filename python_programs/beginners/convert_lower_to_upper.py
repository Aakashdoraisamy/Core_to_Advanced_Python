# 1st way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    ord_val = ord(c)+32 
# --> 65+32=97
    c_val = chr(ord_val) 
# --> chr(97) = 'a'
    print(c_val)
else:
    print("not valid")
    
# 2nd efficient way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    print(chr(ord(c)+32))
else:
    print("not valid")