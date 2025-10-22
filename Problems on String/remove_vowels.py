print("Remove all vowels from string")
s = "Beautiful Day"
vowels = "aeiouAEIOU"
result = ''.join([ch for ch in s if ch not in vowels])
print("Result:", result)
# Output: Btfl Dy