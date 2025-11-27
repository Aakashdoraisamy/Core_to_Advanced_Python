arr = [10, 20, 4, 45, 99, 99]

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)
