arr = [10, 20, 4, 45, 99, 99]

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)


# arr = [10, 20, 4, 45, 99, 99]

# unique_sorted = sorted(set(arr), reverse=True)
# print("Second largest:", unique_sorted[1])


arr = [10, 20, 4, 45, 99, 99]

first = second = third = float('-inf')

for num in arr:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != first and num != second:
        third = num

if third == float('-inf'):
    print("No 3rd largest number found")
else:
    print("Third largest:", third)

