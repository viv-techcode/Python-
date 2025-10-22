arr = [5, 2, 9, 1, 7]
first_min = second_min = float('inf')
first_max = second_max = float('-inf')
for num in arr:
    if num < first_min:
        second_min = first_min
        first_min = num
    elif num < second_min and num != first_min:
        second_min = num

    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num
print(" Second Smallest:", second_min, "Second Largest:", second_max)

# Output: Second Smallest: 2  Second Largest: 7