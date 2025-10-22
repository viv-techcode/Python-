arr = [1, 2, 3, 1, 2, 4, 5, 3]
repeats = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count > 1 and arr[i] not in repeats:
        repeats.append(arr[i])
print("Repeating elements:", repeats)

# Output: Repeating elements: [1, 2, 3]