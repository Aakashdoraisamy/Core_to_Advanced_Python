lst = [1, 2, 3, 4, 5]
# Rotate to the right by 1 (manual)

lst = [1, 2, 3, 4, 5]

last = lst[-1]     # save last element
for i in range(len(lst)-1, 0, -1):
    lst[i] = lst[i-1]  # shift right
lst[0] = last        # put last at first

print(lst)  # [5, 1, 2, 3, 4]


# Rotate to the left by 1 (manual)

lst = [1, 2, 3, 4, 5]

first = lst[0]      # save first element
for i in range(len(lst)-1):
    lst[i] = lst[i+1]  # shift left
lst[-1] = first       # put first at last

print(lst)  # [2, 3, 4, 5, 1]

# Rotate by n positions (left)

lst = [1, 2, 3, 4, 5]
n = 2  # positions to rotate

for _ in range(n):
    first = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    lst[-1] = first

print(lst)  # [3, 4, 5, 1, 2]

# Rotate by n positions (right)

lst = [1, 2, 3, 4, 5]
n = 2  # positions to rotate

for _ in range(n):
    last = lst[-1]
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = last

print(lst)  # [4, 5, 1, 2, 3]


# Using slicing (built-in, simpler)

lst = [1, 2, 3, 4, 5]
n = 2

# left rotation
lst = lst[n:] + lst[:n]
print(lst)  # [3, 4, 5, 1, 2]

# right rotation
lst = lst[-n:] + lst[:-n]
print(lst)  # [4, 5, 1, 2, 3]

lst = [1, 2, 3, 4, 5]
n = 2   # positions to rotate

lst = lst[n:] + lst[:n]
print(lst)  # [3, 4, 5, 1, 2]

