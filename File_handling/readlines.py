# it reads all the lines inside the file
# returns in the form of list with \n

with open('placement.txt','r+') as file:
    line = file.readlines()
    print(line,file.tell())
    print(file.read()) # returns nothing because the cursor stops at the end of the file
    
# ['12345000content111 if not exists\n', 'Error - if file is already exists\n', "FileExistsError: [Error 17] File exists: 'placement.txt'"] 125