def containsDuplicate(nums):
    s = set()
    d = set()
    for i in nums:
        if i in s:
            d.add(i)
            return True
        else:
            s.add(i)
    return False
print(containsDuplicate([1,2,3,1]))