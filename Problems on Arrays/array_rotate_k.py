arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
rotated = arr[-k:] + arr[:-k]
print("Array rotated by", k, ":", rotated)


# Output: Array rotated by 2: [4, 5, 1, 2, 3]