A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

is_subset = True  # assume A is subset

for elem in A:
    if elem not in B:
        is_subset = False
        break

if is_subset:
    print("A is a subset of B")
else:
    print("A is NOT a subset of B")
