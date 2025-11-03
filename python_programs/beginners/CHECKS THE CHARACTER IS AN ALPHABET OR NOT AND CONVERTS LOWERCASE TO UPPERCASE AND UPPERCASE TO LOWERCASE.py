
# CHECKS THE CHARACTER IS AN ALPHABET OR NOT AND CONVERTS LOWERCASE TO UPPERCASE AND UPPERCASE TO LOWERCASE

# 1st way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    ord_val = ord(c)+32 
    c_val = chr(ord_val) 
    print(c_val)
elif c>= 'a' and c <= 'z':
    ord_val = ord(c)-32 
    c_val = chr(ord_val) 
    print(c_val)
else:
    print("Given input is not an alphabet")

# 2nd way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    print(chr(ord(c)+32))
elif c>= 'a' and c <= 'z':
    print(chr(ord(c)-32))
else:
    print("Given input is not an alphabet")