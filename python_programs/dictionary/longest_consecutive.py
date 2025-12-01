def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Start of a new sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            # Count forward sequence
            while current + 1 in num_set:
                current += 1
                length += 1
            
            longest = max(longest, length)
    
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # Output: 4  (1,2,3,4)
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))     # Output: 9  (0 to 8)
print(longest_consecutive([]))                        # Output: 0
