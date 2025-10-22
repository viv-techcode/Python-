arr = [7, 1, 3, 5]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
n = len(arr)
if n % 2 == 0:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
else:
    median = arr[n//2]
print("Median of array:", median)


# Output: Median of array: 4.0