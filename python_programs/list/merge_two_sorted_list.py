list1 = [1, 2, 4]
list2 = [1, 3, 4]

merge = []
i = 0
j = 0

# Merge until one list is exhausted
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merge.append(list1[i])
        i += 1
    else:
        merge.append(list2[j])
        j += 1

# Append remaining elements
while i < len(list1):
    merge.append(list1[i])
    i += 1

while j < len(list2):
    merge.append(list2[j])
    j += 1

print(merge)  # Output: [1, 1, 2, 3, 4, 4]



"""
Perfect! Let’s go step by step, beginner-friendly, for your input:

list1 = [1, 2, 4]
list2 = [1, 3, 4, 5]


Goal: merge them into one sorted list.

Step 0: Initialization
merge = []  # Final merged list
i = 0       # Pointer for list1
j = 0       # Pointer for list2


merge starts empty.

i points to the first element of list1.

j points to the first element of list2.

Step 1: Compare elements while both lists have elements
while i < len(list1) and j < len(list2):


Loop continues as long as neither pointer reached the end.

Iteration 1

i = 0, j = 0

list1[i] = 1, list2[j] = 1

Compare: 1 < 1 → False → go to else

Action: append list2[j] → merge = [1]

Increment j: j = 1

Iteration 2

i = 0, j = 1

list1[i] = 1, list2[j] = 3

Compare: 1 < 3 → True

Action: append list1[i] → merge = [1, 1]

Increment i: i = 1

Iteration 3

i = 1, j = 1

list1[i] = 2, list2[j] = 3

Compare: 2 < 3 → True

Action: append list1[i] → merge = [1, 1, 2]

Increment i: i = 2

Iteration 4

i = 2, j = 1

list1[i] = 4, list2[j] = 3

Compare: 4 < 3 → False → go to else

Action: append list2[j] → merge = [1, 1, 2, 3]

Increment j: j = 2

Iteration 5

i = 2, j = 2

list1[i] = 4, list2[j] = 4

Compare: 4 < 4 → False → go to else

Action: append list2[j] → merge = [1, 1, 2, 3, 4]

Increment j: j = 3

Iteration 6

i = 2, j = 3

list1[i] = 4, list2[j] = 5

Compare: 4 < 5 → True

Action: append list1[i] → merge = [1, 1, 2, 3, 4, 4]

Increment i: i = 3

Now i = len(list1) → exit while loop

Step 2: Append remaining elements
Remaining elements in list1?
while i < len(list1):
    merge.append(list1[i])
    i += 1


i = 3, len(list1) = 3 → no elements left → skip

Remaining elements in list2?
while j < len(list2):
    merge.append(list2[j])
    j += 1


j = 3, len(list2) = 4 → one element left (5)

Append 5 → merge = [1, 1, 2, 3, 4, 4, 5]

Increment j = 4 → loop ends

Step 3: Final merged list
print(merge)  # [1, 1, 2, 3, 4, 4, 5]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        tail = dummy     

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next 