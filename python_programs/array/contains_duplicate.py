def containsDuplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False
print(containsDuplicate([1,2,3]))