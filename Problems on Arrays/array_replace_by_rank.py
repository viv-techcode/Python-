arr = [40, 10, 30, 20]
sorted_arr = []
for num in arr:
    inserted = False
    for i in range(len(sorted_arr)):
        if num < sorted_arr[i]:
            sorted_arr.insert(i, num)
            inserted = True
            break
    if not inserted:
        sorted_arr.append(num)

ranks = []
for num in arr:
    rank = 1
    for val in sorted_arr:
        if val < num:
            rank += 1
    ranks.append(rank)
print("Array elements replaced by their rank:", ranks)


# Output: Array replaced by ranks: [4, 1, 3, 2]