arr = [1, 2, 2, 3, 4, 4, 5]
non_repeats = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        non_repeats.append(arr[i])
print("Non-repeating elements:", non_repeats)


# Output: Non-repeating elements: [5]