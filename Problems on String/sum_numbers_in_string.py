print("Sum numbers in string")
s = "abc12xy3"
total = sum(int(ch) for ch in s if ch.isdigit())
print("Sum:", total)
# Output: 6