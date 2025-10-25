## to read the number of characters inside the file also without build in method len

file = open('placement.txt','r')
count = 0
for line in file:
    for char in line:
        count += 1 
file.close()
print('Count of file:', count)

# direct way
count = 0
with open('placement.txt') as file: # default filemode is read
# with open('placement.txt','r') as file:
    content = file.read()
    for char in content:
        count+=1
print('Count of File:',count)

#second way
file = open('placement.txt','r')
count = 0
content = file.read()
for char in content:
    count+=1
print('Count of File:',count)

## to read the characters without inside the file

file = open('placement.txt','r')
content = file.read()
words = content.split()
char_count = len(content)
words_count = len(words)
print(words)
print(f'Character Count:{char_count} Words Count:{words_count}')
file.close()