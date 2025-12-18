s = "madam"

i, j = 0, len(s) - 1
flag = True

while i < j:
    if s[i] != s[j]:
        flag = False
        break
    i += 1
    j -= 1

print(flag)
