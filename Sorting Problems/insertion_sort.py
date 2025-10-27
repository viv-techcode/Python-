print("Insertion Sort Algorithm")

arr = [12, 11, 13, 5, 6]
print("Original Array:", arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted Array:", arr)


# Output: [5, 6, 11, 12, 13]