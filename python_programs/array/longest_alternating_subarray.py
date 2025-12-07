arr = [1, 2, 3, 4, 5, 7, 8, 10, 11]

max_len = 1
current = 1

for i in range(1, len(arr)):
    if (arr[i] % 2) != (arr[i-1] % 2):  # alternates
        current += 1
        max_len = max(max_len, current)
    else:
        current = 1

print("Longest alternating subarray length:", max_len)
