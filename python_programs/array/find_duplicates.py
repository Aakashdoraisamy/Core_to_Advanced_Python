arr = [1, 2, 3, 2, 4, 1]

seen = set()
dups = set()

for x in arr:
    if x in seen:
        dups.add(x)
    else:
        seen.add(x)

print(list(dups))
