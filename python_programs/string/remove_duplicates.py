#1ST WAY

s = input("enter any string:")

output = ''

for ch in s:

    if ch not in output:

        output = ''.join(sorted(output+ch))

print(output)

#2ND WAY

s = input("enter any string:")

l = []
for ch in s:

    if ch not in l:

        l.append(ch)

        output = ''.join(sorted(l))

print(output)


#3RD WAY

s = input("enter any string:")

s1 = set(s)

output = ''.join(s1)

print(output)