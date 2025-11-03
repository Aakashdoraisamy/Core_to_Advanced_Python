l = [1,2,3,4,5,12,43,90,87,1,2,5,9,8]
l1 = int(input("Enter a value to find the occurence: "))
count = 0
for i in l:
    if i == l1:
        count+=1
print(f"{l1} is found {count} times in the list")