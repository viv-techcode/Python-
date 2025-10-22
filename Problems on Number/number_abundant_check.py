#  Check if the number is abundant number or not


print(" Abundant number check")
n = 12
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
print("Sum proper divisors:", s, "Is abundant?", s > n)	


# Output: 12 is Abundant 