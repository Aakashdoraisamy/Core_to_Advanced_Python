s = "aakash"
visited = ""  # to store characters we already counted

for ch in s:
    if ch not in visited:  # count only first time
        count = 0
        for c in s:       # loop through string to count occurrences
            if c == ch:
                count += 1
        print(ch, ":", count)
        visited += ch    # mark this character as counted


"""
Dry Run for "aakash"

ch = 'a' → not in visited → count 'a' in string → 3 → print → add 'a' to visited

ch = 'a' → in visited → skip

ch = 'k' → not in visited → count 'k' → 1 → print → add 'k' to visited

ch = 'a' → in visited → skip

ch = 's' → not in visited → count 's' → 1 → print → add 's' to visited

ch = 'h' → not in visited → count 'h' → 1 → print → add 'h' to visited

a : 3
k : 1
s : 1
h : 1

"""

# Using ASCII Array (without dict, faster)

s = "aakash"
freq = [0] * 256   # array for all ASCII characters

for ch in s:
    freq[ord(ch)] += 1

for i in range(256):
    if freq[i] > 0:
        print(chr(i), ":", freq[i])


# Using count() (built-in)

s = "aakash"
for ch in s:
    if s.index(ch) == s.find(ch):   # first time seeing this char
        print(ch, ":", s.count(ch))

# Without Dictionary (nested loops, only string)

s = "aakash"
visited = ""

for i in range(len(s)):
    if s[i] not in visited:  # avoid recounting
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        print(s[i], ":", count)
        visited += s[i]


# Using Dictionary (most common)

s = "aakash"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, ":", freq[key])

s = "interview"

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
