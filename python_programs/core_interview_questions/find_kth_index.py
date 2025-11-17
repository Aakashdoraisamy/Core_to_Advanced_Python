def find_balanced_index(s):
    open_count = 0
    close_count = 0

    for i, char in enumerate(s):
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        
        if open_count == close_count:
            return i  # Found the index where '(' = ')'
    
    return -1  # No such index

# Example
s = "(()())()"
print(find_balanced_index(s))  # Output: 5
