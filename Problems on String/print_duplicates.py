

print("Print duplicate characters")

s = "programming"
dupes = {ch for ch in s if s.count(ch) > 1}
print("Duplicates:", dupes)

# Output: {'r', 'g', 'm'}