file = open('placement.txt','x')

""" 
x - creates a file if not exists
Error - if file is already exists
FileExistsError: [Error 17] File exists: 'placement.txt'
"""

## Read

file = open('placement.txt','r') # if file exists then read mode is possible if not it will raise error as file not found
content = file.read() # reads the complete file and returns string
print(content)
file.close()

## write

file = open('placement.txt','r') 
file.write('hello') 
print('file operation was done')
file.close()