"""
a ---> filemode

if file no exists creates a new file
by default cursor position will be end of the file
only write method is possible
seek won't work for write operations

a+ ----> filemode

Directly read,operation is not possible
why ?
    by default cursor located at the last

"""

# # append 
# append if file is not present it will creates new file

# f = open('abc.txt','a')
# # f.read()
# f.write('hello\nhi\n') 
# print(f.tell())
# f.seek(0)
# print(f.read())

# Traceback (most recent call last):
#   File "C:\Users\VarunAakash\OneDrive\Desktop\Pyspyder_class\File_handling\append.py", line 6, in <module>
#     f.read()
# io.UnsupportedOperation: not readable


## apend +

f = open('abc.txt','a+')
f.write('hello\nhi\n') # add end of the file and it won't replace 
print(f.tell())
f.seek(0)
print(f.read())