s = input('Enter a string with spaces:')
l = []
word = ''
for char in s:
    if char != ' ':
        word += char
    else:
        l.append(word)
        word = ''
l.append(word) # to append the last word
print(l)
