def issubstring(t,s):
    p1 = 0
    p2 = 0
    while p1<len(t) and p2<len(s):
        if t[p1] == s[p2]:
            p1+=1
            p2+=1
        else:
            p1+=1
            
    if p2 == len(s):
        return True
    else:
        return False
print(issubstring('abcdef','ab'))










# Exact step-by-step trace for issubstring('abcdef', 'ab')

# Initial values:

# t = "abcdef" → len(t) = 6

# s = "ab" → len(s) = 2

# p1 = 0, p2 = 0

# We will show each loop iteration (values shown before comparison):

# Iteration 1

# p1 = 0, p2 = 0

# t[p1] = 'a', s[p2] = 'a'

# Compare: 'a' == 'a' → True

# Action: p1 += 1 → p1 = 1, p2 += 1 → p2 = 1

# Iteration 2

# p1 = 1, p2 = 1

# t[p1] = 'b', s[p2] = 'b'

# Compare: 'b' == 'b' → True

# Action: p1 += 1 → p1 = 2, p2 += 1 → p2 = 2

# Now check loop condition: p2 < len(s)? → 2 < 2 is False → loop stops.

# After loop: p2 == len(s) → 2 == 2 → True → function returns True.

# So print(issubstring('abcdef','ab')) prints True.

# A few quick examples to see the difference

# issubstring("abcdef", "ace") → True (a, c, e appear in t in order)

# issubstring("abcdef", "cae") → False (c appears after a, order not preserved)

# issubstring("hello", "ll") → True (two l's appear in order)

# Note: For contiguous substring checking (characters must be next to each other), this function is not correct — it allows gaps. For a contiguous check you would need a different approach (or just s in t).

# Complexity

# Time: O(len(t)) in the worst case (you scan t once).

# Space: O(1) extra memory (only two integer pointers).