s = input("enter any character:")

output = ''

d = {}

for ch in s:

    d[ch] = d.get(ch,0)+1

for k,v in sorted(d.items()):

    output = output+str(v)+k

print(output)


#REVERSE IT AAABBC to A3B2C1

s = input("enter any character:")

output = ''

d = {}

for ch in s:

    d[ch] = d.get(ch,0)+1

for k,v in sorted(d.items()):

    output = output+k+str(v)

print(output)
