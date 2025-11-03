string = "Python Programming"
print(string[::-1])

# 2ND WAY

s = input('Enter a String:')
rev = s[-1:-len(s)-1:-1]
for char in rev:
    print(char)
    
# 3rd way

s = "Aakash"
print("".join(reversed(s)))

