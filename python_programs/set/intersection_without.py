A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

intersection = set()

for elem in A:
    if elem in B:    # check manually
        intersection.add(elem)

print("Intersection:", intersection)  # {3, 4}


# Intersection (common elements, no duplicates)

A = [1, 2, 3, 4, 2, 3]
B = [3, 4, 5, 6, 3, 6]

intersection = []

for elem in A:
    if elem in B and elem not in intersection:
        intersection.append(elem)

print("Intersection:", intersection)  # [3, 4]
