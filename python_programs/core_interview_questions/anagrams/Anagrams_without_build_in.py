# 1st way

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    count1 = [0] * 26
    count2 = [0] * 26

    for ch in s1:
        count1[ord(ch) - ord('a')] += 1

    for ch in s2:
        count2[ord(ch) - ord('a')] += 1

    if count1 == count2:
        print("Anagrams")
    else:
        print("Not Anagrams")


# 2nd way

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

def is_anagram(s1, s2):
    # Step 1: Length check
    if len(s1) != len(s2):
        return False
    
    # Step 2: Frequency counting
    freq = {}
    
    # Count characters in s1
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    # Decrease counts using s2
    for ch in s2:
        if ch not in freq:
            return False   # char not present
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]   # cleanup
    
    # Step 3: Check final frequency
    return len(freq) == 0

if is_anagram(s1, s2):
    print("Both strings are Anagrams")
else:
    print("Both strings are Not Anagrams")
