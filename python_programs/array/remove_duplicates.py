# return after removing duplicates how many unique items
def fun(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1 
print(fun([1,1,2,2,3])) # 3



# RETURN AFTER REMOVING DUPLICATES THE UNIQUE LIST

def fun(nums):
    if not nums:  # handle empty list
        return []
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    # Slice the list to include only unique elements
    return nums[:i+1] # [1,2,3]

print(fun([1,1,2,2,3]))


arr = [1, 2, 2, 3, 1]
res = []

for x in arr:
    if x not in res:
        res.append(x)

print(res)
