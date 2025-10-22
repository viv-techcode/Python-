
print("Remove duplicates")

s = "banana"
result = ''.join(sorted(set(s), key=s.index))
print("Result:", result)

# Output: ban