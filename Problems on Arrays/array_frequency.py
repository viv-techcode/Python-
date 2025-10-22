arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Frequency of elements:", freq)


# Output: Frequency of elements: {1: 2, 2: 3, 3: 1, 4: 1}