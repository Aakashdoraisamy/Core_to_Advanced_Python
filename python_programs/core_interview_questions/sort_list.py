my_list = [5, 2, 9, 1, 7]
n = len(my_list)
for i in range(n):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            # Swap if elements are in wrong order
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)














# Output: [1, 2, 5, 7, 9]


# List:
# my_list = [5, 2, 9, 1, 7]

# Step 0: Number the positions
# Index:   0  1  2  3  4
# Value:   5  2  9  1  7

# PASS 1 (i = 0) → compare j = 0 to 3 (n-i-1 = 4)

# j = 0: compare my_list[0] and my_list[1] → 5 > 2 → swap

# [2, 5, 9, 1, 7]


# j = 1: compare my_list[1] and my_list[2] → 5 > 9 → no swap

# [2, 5, 9, 1, 7]


# j = 2: compare my_list[2] and my_list[3] → 9 > 1 → swap

# [2, 5, 1, 9, 7]


# j = 3: compare my_list[3] and my_list[4] → 9 > 7 → swap

# [2, 5, 1, 7, 9]


# ✅ After Pass 1, 9 is in correct position (index 4)

# PASS 2 (i = 1) → compare j = 0 to 2 (n-i-1 = 3)

# j = 0: compare my_list[0] and my_list[1] → 2 > 5 → no swap

# [2, 5, 1, 7, 9]


# j = 1: compare my_list[1] and my_list[2] → 5 > 1 → swap

# [2, 1, 5, 7, 9]


# j = 2: compare my_list[2] and my_list[3] → 5 > 7 → no swap

# [2, 1, 5, 7, 9]


# ✅ After Pass 2, 7 is in correct position (index 3)

# PASS 3 (i = 2) → compare j = 0 to 1 (n-i-1 = 2)

# j = 0: compare my_list[0] and my_list[1] → 2 > 1 → swap

# [1, 2, 5, 7, 9]


# j = 1: compare my_list[1] and my_list[2] → 2 > 5 → no swap

# [1, 2, 5, 7, 9]


# ✅ After Pass 3, 5 is in correct position (index 2)

# PASS 4 (i = 3) → compare j = 0 to 0 (n-i-1 = 1)

# j = 0: compare my_list[0] and my_list[1] → 1 > 2 → no swap

# [1, 2, 5, 7, 9]


# ✅ After Pass 4, 2 is in correct position (index 1)

# PASS 5 (i = 4) → compare j = 0 to -1

# Inner loop doesn’t run

# List is fully sorted

# Final Sorted List
# [1, 2, 5, 7, 9]

# ✅ Mathematical Summary
# Pass (i)	j values	List after swaps
# 1	0,1,2,3	[2, 5, 1, 7, 9]
# 2	0,1,2	[2, 1, 5, 7, 9]
# 3	0,1	[1, 2, 5, 7, 9]
# 4	0	[1, 2, 5, 7, 9]
# 5	-	[1, 2, 5, 7, 9] (sorted)