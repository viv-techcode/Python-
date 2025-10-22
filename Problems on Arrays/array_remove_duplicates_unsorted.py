arr = [4, 2, 1, 2, 3, 4, 5, 1]
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print("Array after removing duplicates (unsorted):", unique)


# Output: Array after removing duplicates: [4, 2, 1, 3, 5]
