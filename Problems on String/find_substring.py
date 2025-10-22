

print("Find substring position")

s = "Hello World"
sub = "World"
pos = s.find(sub)
if pos != -1:
    print(f"'{sub}' found at position {pos}")
else:
    print("Not found")

# Output: 'World' found at position 6