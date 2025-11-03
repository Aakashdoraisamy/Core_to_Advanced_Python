s = input('enter some string vaale alphabets follwed by digits:')

output = ''

for ch in s:

    if ch.isalpha():

        x = ch

    else:

        d = int(ch)

        output = output+x*d

print(output)