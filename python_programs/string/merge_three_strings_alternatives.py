s1 = input("enter a string 1:")

s2 = input("enter a string 2:")

s3 = input("enter a string 3:")

output = ''

i,j,k = 0,0,0

while i<len(s1) or j<len(s2) or k<len(s3):

    if i<len(s1):

        output = output+s1[i]

        i = i+1

    if j<len(s2):

        output = output+s2[j]

        j = j+1
 
    if k<len(s3):

        output = output+s3[k]

        k = k+1
 
print(output)