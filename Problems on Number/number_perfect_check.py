# Check if a number is perfect number

print(" Check perfect number")
n = 28
print("Number:", n)
s = 0
i = 1
while i*i <= n:
    if n % i == 0:
        if i != n:
            s += i
        j = n//i
        if j != i and j != n:
            s += j
    i += 1
print("Is perfect?", s == n)

# Output: 28 is Perfect 