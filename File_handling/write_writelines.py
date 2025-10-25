"""
w

write replace the old content and creates new file

1) creates new file and writes the content w+
    - creates new file,(write and read) Access

steps to follow:

1) we should not use read(),readline(),readlines() direct access
2) after write,writeline we can perform read()
3) but before performing read operation we need to move the cursor to 0th position by using seek

"""


with open('placement.txt','w+') as file:
    l = ['python is easier than the other programming language\n','ok\n','Data Science\n']
    file.writelines(l)
    print('File writing was done....')

with open('placement.txt','r+') as file:
    l = ['python is easier than the other programming language\n','ok\n','Data Science\n']
    file.writelines(l)
    print('File writing was done....') # it just updates the old
    
with open('placement.txt','w') as file:
    l = ['python is easier than the other programming language\n','ok\n','Data Science\n']
    file.writelines(l)
    print('File writing was done....') # # it replaces the entire file
    
# in write mode if the file is not exists it will creates a new file and writes the content 

with open('python.txt','w') as file:
    l = ['python is easier than the other programming language\n','ok\n','Data Science\n']
    file.writelines(l)
    print('File writing was done....')
    

# it raise error because we didn't give persmission for read

with open('python.txt','w') as file:
    file.read()
    
#   File "C:\Users\VarunAakash\OneDrive\Desktop\Pyspyder_class\File_handling\writelines.py", line 25, in <module>
#     file.read()
# io.UnsupportedOperation: not readable


with open('python.txt','r+') as file:
    file.write('w')
# it writes the content the from the file replaces the start cursor(0)
    
with open('python.txt','w+') as file:
    # content = file.read()
    # print(content)
# when it comes in w+ we can't performm directly read it clears all and returns the empty file
    l = ['python is easier than the other programming language\n','ok\n','Data Science\n']
    file.writelines(l)
    print(file.tell()) # it gives end of the file cursor
    file.seek(0) # it change to first index
    print(file.read())
    
