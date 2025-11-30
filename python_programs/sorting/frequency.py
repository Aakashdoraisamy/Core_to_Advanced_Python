from collections import Counter

arr = [1,1,2,3,3,3,2]
freq = Counter(arr)

sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
print(sorted_arr)


# Input → [1,1,2,3,3,3,2]
# Output → [3,3,3,1,1,2,2]