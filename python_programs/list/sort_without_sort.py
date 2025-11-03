lst = [5, 2, 9, 1, 5, 6]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            # swap elements
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list:", lst)

"""
🔹 Logic Step by Step

Outer loop (i)

Goes through each element in the list

i = 0 → first element 5

i = 1 → second element 2

…and so on

Inner loop (j)

Compares lst[i] with all elements after it

j = i + 1 → avoids comparing with previous elements

Comparison and swap

if lst[i] > lst[j]:
    lst[i], lst[j] = lst[j], lst[i]


If current element (lst[i]) is bigger than the element after it (lst[j])

Swap them so smaller number moves to front

Repeat

After each pass of the outer loop, the smallest remaining element moves to its correct position

Continue until the last element → the list becomes sorted

🔹 Dry Run (Step by Step)

Initial list: [5, 2, 9, 1, 5, 6]

i=0 → compare 5 with [2, 9, 1, 5, 6]

5>2 → swap → [2, 5, 9, 1, 5, 6]

2>9 → no swap

2>1 → swap → [1, 5, 9, 2, 5, 6]

… end of inner loop → smallest element 1 at index 0

i=1 → compare 5 with [9, 2, 5, 6]

5>9 → no swap

5>2 → swap → [1, 2, 9, 5, 5, 6]

… end of inner loop → second smallest element 2 at index 1

Continue for i=2,3,4 → finally list becomes [1, 2, 5, 5, 6, 9]
"""