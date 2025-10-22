
print("Remove chars from first string present in second")

s1 = "computer"
s2 = "cat"
result = ''.join([ch for ch in s1 if ch not in s2])
print("Result:", result)

# Output: ompuer