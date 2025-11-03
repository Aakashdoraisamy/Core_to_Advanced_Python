    
# without slice notation

s = input('Enter a String:')
rev = ''
for char in s:
    rev = char + rev
print(rev)

# using while loop

s = "Aakash"
rev = ""
i = len(s) - 1
while i >= 0:
    rev += s[i]
    i -= 1
print(rev)

# using recursion

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("Aakash"))
