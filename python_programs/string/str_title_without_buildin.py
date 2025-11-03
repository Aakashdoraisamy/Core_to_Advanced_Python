s = "heLLo woRLd pYtHon"
result = ""
make_upper = True   # first character should be uppercase

for ch in s:
    if ch == " ":  # when space found
        result += ch
        make_upper = True
    else:
        if make_upper:  # first letter of word
            # convert to uppercase manually
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch
            make_upper = False
        else:  # other letters lowercase
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch

print(result)   # Hello World Python
