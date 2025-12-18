s = "programming"
seen = set()

for ch in s:
    if ch in seen:
        print("Duplicate character:", ch)
        break
    seen.add(ch)
else:
    print("No duplicate characters found.")