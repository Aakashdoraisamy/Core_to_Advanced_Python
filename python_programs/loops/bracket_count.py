s = "(()(()())(()"
count_open = 0

for ch in s:
    if ch == '(':
        count_open += 1

print(count_open)
