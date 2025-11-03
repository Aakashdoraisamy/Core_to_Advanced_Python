# Input string
input_str = "123asd3435eetyu=09egr"

# Create an empty string to store the result
result = ""

# Iterate through each character in the input string
for char in input_str:
    # Check if the character is a letter
    if char.isalpha():
        # Add the letter to the result string
        result += char

# Print the result
print(result)
