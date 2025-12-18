s = "Python programming interview questions"

words = s.split()
longest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w

print(longest)
