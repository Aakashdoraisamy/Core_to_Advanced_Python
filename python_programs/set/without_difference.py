A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

difference = set()

for elem in A:
    if elem not in B:
        difference.add(elem)

print("Difference (A - B):", difference)  # {1, 2}


# Example (with duplicates in lists)

A = [1, 2, 3, 4, 2, 3]
B = [3, 4, 5, 6, 3, 6]

difference = []

for elem in A:
    if elem not in B and elem not in difference:
        difference.append(elem)

print("Difference (A - B):", difference)  # [1, 2]
