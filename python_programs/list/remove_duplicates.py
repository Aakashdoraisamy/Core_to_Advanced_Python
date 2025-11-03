lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print(unique_lst)   # e.g., [1, 2, 3, 4, 5]


# Using for loop (preserve order)

unique_lst = []
for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print(unique_lst)   # [1, 2, 3, 4, 5]


# Using dictionary keys (preserve order )

unique_lst = list(dict.fromkeys(lst))
print(unique_lst)   # [1, 2, 2, 3, 4, 4, 5] → [1,2,3,4,5]


# Using list comprehension (with a helper list)

unique_lst = []
[unique_lst.append(x) for x in lst if x not in unique_lst]
print(unique_lst)   # [1, 2, 3, 4, 5]


lst = [1, 2, 2, 3, 4, 4, 5]
i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        # check for duplicate and remove
        if lst[i] == lst[j]:
            lst.pop(j)  # remove duplicate
        else:
            j += 1
    i += 1

print(lst)   # [1, 2, 3, 4, 5]

