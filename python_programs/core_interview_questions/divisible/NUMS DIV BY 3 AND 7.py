start = int(input('Enter Start Range:'))
end = int(input('Enter End Range:'))
count = 0
for i in range(start, end+1):
    if i%3 == 0 and i%7 == 0:
        count+=1
print(f'Count of numbers divisible by 3 and 7 from {start} to {end} is : {count}')


# if we give print inside the loop it will print all the numbers which are divisible by 3 and 7 it will return 0 until count increases like
# start = 1
# end = 20
# count 0
# 0
# 0
# .
# .
# until 20
# then 21 will divisible by 3 and 7 so count will increase to 1
# and then 1
# 1
# 1
# .
# .
# until end so we need to give print outside the loop