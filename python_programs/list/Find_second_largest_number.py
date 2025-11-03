lst = [10, 5, 20, 8, 20, 2]

# Using sort (simplest)

lst_sorted = sorted(lst, reverse=True)  # sort descending
for num in lst_sorted:
    if num < lst_sorted[0]:  # first smaller than max
        print("Second largest:", num)
        break

# Using set + sort (remove duplicates first)

unique_lst = list(set(lst))  # remove duplicates
unique_lst.sort(reverse=True)
print("Second largest:", unique_lst[1])

# Using two variables (without sort)

lst = [10, 5, 20, 8, 20, 2]

first = second = float('-inf')

for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)


# Using remove max method (manual)

lst = [10, 5, 20, 8, 20, 2]
max_num = max(lst)
while max_num in lst:
    lst.remove(max_num)  # remove all occurrences of largest
print("Second largest:", max(lst))







