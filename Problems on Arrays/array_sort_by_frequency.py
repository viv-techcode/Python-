arr = [1, 2, 2, 3, 3, 3, 4]
freq = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    freq.append((arr[i], count))

# Sort by frequency (descending)
for i in range(len(freq)):
    for j in range(i + 1, len(freq)):
        if freq[i][1] < freq[j][1]:
            freq[i], freq[j] = freq[j], freq[i]

result = []
for val, count in freq:
    if val not in result:
        result += [val] * count
print("Array sorted by frequency:", result)


# Output: Array sorted by frequency: [3, 3, 3, 2, 2, 1, 4]