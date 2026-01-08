arr = [1, 3, 5, 7, 9, 11]
target = 7

low, high = 0, len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
