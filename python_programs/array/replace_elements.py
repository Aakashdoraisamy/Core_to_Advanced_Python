
def replaceElements(arr):
    rightmax = -1
    for i in range(len(arr)-1,-1,-1):
        tempmax = max(rightmax,arr[i])
        arr[i] = rightmax
        rightmax = tempmax
    return arr
print(replaceElements([17,18,5,4,6,1]))

"""
Initialize

rightmax = -1


Start loop from last element to first
range(len(arr)-1, -1, -1) → indices: 5,4,3,2,1,0

🔹 i = 5 (last element = 1)

tempmax = max(-1, 1) = 1

arr[5] = -1 → arr = [17, 18, 5, 4, 6, -1]

rightmax = 1

🔹 i = 4 (element = 6)

tempmax = max(1, 6) = 6

arr[4] = 1 → arr = [17, 18, 5, 4, 1, -1]

rightmax = 6

🔹 i = 3 (element = 4)

tempmax = max(6, 4) = 6

arr[3] = 6 → arr = [17, 18, 5, 6, 1, -1]

rightmax = 6

🔹 i = 2 (element = 5)

tempmax = max(6, 5) = 6

arr[2] = 6 → arr = [17, 18, 6, 6, 1, -1]

rightmax = 6

🔹 i = 1 (element = 18)

tempmax = max(6, 18) = 18

arr[1] = 6 → arr = [17, 6, 6, 6, 1, -1]

rightmax = 18

🔹 i = 0 (element = 17)

tempmax = max(18, 17) = 18

arr[0] = 18 → arr = [18, 6, 6, 6, 1, -1]

rightmax = 18
"""