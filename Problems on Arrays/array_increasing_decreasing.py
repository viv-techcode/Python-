arr = [5, 2, 9, 1, 7]
# Increasing order
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Increasing order:", arr)
# Decreasing order
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Decreasing order:", arr)


# Output: Increasing: [1, 2, 5, 7, 9], Decreasing: [9, 7, 5, 2, 1]