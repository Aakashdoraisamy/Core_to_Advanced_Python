# LIST COMPRESESION

# NORMAL CODE

l = int(input('Enter Your Input:'))
l1 = []
for i in range(1,l+1):
    l1.append(i)
print(l1)

l = [i for i in range(1,7)]
print(l)

l = [i*i for i in range(1,7)]
print(l)

# NORMAL CODE

n = int(input('Enter Your range:'))
l = []
for i in range(1, n+1):
    num = int(input(f'Enter number {i}: '))
    l.append(num)
print(l)

# 1ST WAY

start = int(input('Enter Start range:'))
end = int(input('Enter end range:'))
step = int(input('Enter step range:'))
l = [i for i in range(start,end+1,step)]
print(l)

# 2ND WAY

n = int(input('Enter Your range:'))
l = [int(input('Enter Your Number:')) for i in range(1,n+1)]
print(l)

# 3RD VALUE

print([int(input('enter Your numbers:')) for i in range(1,int(input('Enter n Value:')))])


# RUN THE LOOP FROM 1 TO 10 IN LIST COMPRENSION ONLY EVEN NUMBERS

# NORMAL CODE

n = int(input('Enter Your range:'))
l1 = []
for i in range(1,n+1):
    if i % 2 == 0:
        l1.append(i)
print(l1)

# # LIST COMPRENSION CODE

# 1ST WAY
n = int(input('Enter Your range:'))
l = [i for i in range(1,n+1) if i%2==0]
print(l)

# # 2ND WAY

l = [i for i in range(1,int(input('Enter Your range:'))+1) if i%2==0]
print(l)




