start = int(input('Enter Start Value:'))
end = int(input('Enter End Value:'))
count = 0
while start<=end:
    if start%3 == 0 and start%8 == 0:
        print(start)
        count+=1
    start+=1
print(f'Count of numbers divisible by 3 and 8 from {start} to {end} is : {count}')