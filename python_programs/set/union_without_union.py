A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = set()  # create empty set

# Add all elements from A
for elem in A:
    union.add(elem)

# Add elements from B
for elem in B:
    union.add(elem)

print("Union:", union)  # {1, 2, 3, 4, 5, 6}


# Example (with duplicates in lists)

# Union (no duplicates)

A = [1, 2, 3, 4, 2, 3]
B = [3, 4, 5, 6, 3, 6]

union = []

for elem in A:
    if elem not in union:
        union.append(elem)

for elem in B:
    if elem not in union:
        union.append(elem)

print("Union:", union)  # [1, 2, 3, 4, 5, 6]
