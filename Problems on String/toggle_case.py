
print("Toggle case of characters")
s = "PyThOn"
result = ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in s])

print("Result:", result)

# Output: pYtHoN