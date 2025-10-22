print("Non-repeating characters")
s = "aabbcdde"
for ch in s:
    if s.count(ch) == 1:
        print(ch, end=' ')
# Output: c e