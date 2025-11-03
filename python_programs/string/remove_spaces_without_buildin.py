s = "  Hello   World Python  "
result = ""

for ch in s:        # check each character
    if ch != " ":   # only keep non-space characters
        result += ch

print(result)   # HelloWorldPython



# Remove only leading and trailing spaces (manual strip)

s = "   Hello   World   "
start = 0
end = len(s) - 1

# find first non-space
while start < len(s) and s[start] == " ":
    start += 1

# find last non-space
while end >= 0 and s[end] == " ":
    end -= 1

# build result
result = ""
for i in range(start, end + 1):
    result += s[i]

print(result)   # Hello   World
