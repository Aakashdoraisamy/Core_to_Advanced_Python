s = "aakash"

for i in range(len(s)):
    repeat = False
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            repeat = True
            break
    if not repeat:
        print("First non-repeating:", s[i])
        break


s = "aakash"
freq = {}

# count characters
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print("First non-repeating:", ch)
        break
