s1 = input("enter a s1 value:")

s2 = input("enter a s2 value:")

i,j = 0,0

output = ''

while i<len(s1) or j<len(s2):

    output = output+s1[i]+s2[j]

    i = i+1

    j = j+1

print(output)


#TO OVERCOME FROM INDEX OUTOFRANGE

s1 = input("Enter a string 1 value:")

s2 = input("Enter a string 2 value:")

i,j = 0,0

output = ''

while i<len(s1) or j<len(s2):

    if i<len(s1):

        output = output+s1[i]

        i = i+1

    if j<len(s2):

        output = output+s2[j]

        j = j+1

print(output)