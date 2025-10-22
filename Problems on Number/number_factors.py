# Factors of a given number


print(" Factors")

n = 28
print("Number:", n)

factors = []
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)

print("Factors:", factors)


# Output: Number: 28 Factors: [1, 2, 4, 7, 14, 28]