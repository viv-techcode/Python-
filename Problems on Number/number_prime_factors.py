#  Print all prime factors of the given number


print(" Prime factors")
n = 315
print("Number:", n)
num = n
pf = []
i = 2
while i*i <= num:
    while num % i == 0:
        pf.append(i)
        num //= i
    i += 1
if num > 1:
    pf.append(num)
print("Prime factors:", pf)


# Output: Prime factors of 60: [2,3,5]