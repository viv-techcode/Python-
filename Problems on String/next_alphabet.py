
print("Shift each letter to next alphabet")

s = "abcXYZ"
result = ''.join([chr(((ord(ch) - 65 + 1) % 26) + 65) if ch.isupper()
                  else chr(((ord(ch) - 97 + 1) % 26) + 97) if ch.islower()
                  else ch for ch in s])
print("Result:", result)

# Output: bcdYZA