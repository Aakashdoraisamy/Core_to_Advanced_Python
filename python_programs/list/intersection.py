a = [1, 2, 3, 4]
b = [3, 4, 5]

res = []

for x in a:
    if x in b and x not in res:
        res.append(x)

print(res)
