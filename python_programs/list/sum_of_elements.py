#for loop

lst = [1, 2, 3, 4, 5]
total = 0
for num in lst:
    total += num
print("Sum:", total)   # 15

# while loop

total = 0
i = 0
while i < len(lst):
    total += lst[i]
    i += 1
print("Sum:", total)

# using sum

print("Sum:", sum(lst))

# recursion

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print("Sum:", sum_list(lst))

# Using for loop with index

total = 0
for i in range(len(lst)):
    total += lst[i]
print("Sum:", total)
