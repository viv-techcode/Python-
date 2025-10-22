# Find all Palindrome numbers in a given range


print(" Palindromes in range 1..200")
res = []
for num in range(1,201):
    t = num
    r = 0
    while t>0:
        r = r*10 + t%10
        t //= 10
    if r == num:
        res.append(num)
print("Palindromes:", res)
	

# Output: Palindromes between 1–200: [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191]
