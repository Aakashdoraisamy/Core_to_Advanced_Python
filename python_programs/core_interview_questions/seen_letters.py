def repeatedCharacter(s):
    seen_letters = []
    for c in s:
        if c in seen_letters:
            return c
        else:
            seen_letters.append(c)
print(repeatedCharacter("abccbaacz"))  # Output: "c"