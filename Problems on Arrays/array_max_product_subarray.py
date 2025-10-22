arr = [2, 3, -2, 4]
max_product = arr[0]
for i in range(len(arr)):
    product = arr[i]
    for j in range(i + 1, len(arr)):
        product *= arr[j]
        if product > max_product:
            max_product = product
print("Maximum product subarray value:", max_product)



# Output: Maximum product subarray value: 6