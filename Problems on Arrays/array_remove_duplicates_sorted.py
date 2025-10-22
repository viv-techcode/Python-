arr = [1, 1, 2, 2, 3, 4, 4, 5]
unique = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        unique.append(arr[i])
print("Array after removing duplicates (sorted):", unique)


# Output: Array after removing duplicates: [1, 2, 3, 4, 5]

