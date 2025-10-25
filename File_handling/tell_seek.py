## tell

file = open('placement.txt','r+')
cursor = file.tell() # return int
print(cursor) # by default it starts from 0
# file.read()
file.write('123456') # 6 the cursor starts from 6 because we used here write operation
cursor = file.tell()
print(cursor)
file.close()


## seek 
# it is used to move the cursor

file = open('placement.txt','r+')
file.seek(5)
file.write('000content111')
print('Updation completed....')
file.close()


# file = open('placement.txt','r+')
# if the filepath is not exists throughs filenotfound error because it is read+write without file how can we read it is possible in w+
