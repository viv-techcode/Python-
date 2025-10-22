arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
# Left rotation
left_rot = arr[k:] + arr[:k]
# Right rotation
right_rot = arr[-k:] + arr[:-k]
print("Left rotation:", left_rot)
print("Right rotation:", right_rot)


# Output: Left rotation: [3, 4, 5, 1, 2]   Right rotation: [4, 5, 1, 2, 3]