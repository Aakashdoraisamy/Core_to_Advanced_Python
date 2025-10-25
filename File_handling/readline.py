# by using read line we can extract only first line
# by read operation the cursor moves at the end of the line
# return type for readline is string

with open('placement.txt','r+') as file:
    line = file.readline()
    print(line,file.tell())
    line = file.readline()
    print(line,file.tell())
    
# 12345000content111 if not exists
#  34
# Error - if file is already exists
#  69
