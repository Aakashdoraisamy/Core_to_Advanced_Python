t = (0, 1, 7, 0, 3, 4)

result = []
count_zero = 0

for x in t:
    if x == 0:
        count_zero += 1      # count zeros
    else:
        result.append(x)     # add non-zero values

# append zeros at the end
for _ in range(count_zero):
    result.append(0)

print(tuple(result))
