# Input list of consecutive numbers
numbers = [1, 2, 3, 4, 5, 6]

# Create a list to store the result
result = []

# Iterate through the list, summing consecutive pairs
for i in range(1, len(numbers), 2):
    sum_pair = numbers[i-1] + numbers[i]
    result.append(sum_pair)

# Print the result
print(result)
