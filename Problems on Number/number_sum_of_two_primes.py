
#  Can a number be expressed as a sum of two prime numbers 


print(" Express as sum of two primes (example n=34)")
n = 34
print("Number:", n)
found_pair = None
# simple check for primes function
def is_prime_func(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
for i in range(2, n//2 + 1):
    if is_prime_func(i) and is_prime_func(n-i):
        found_pair = (i, n-i)
        break
print("Pair found:", found_pair)


# Output: Pair found: (3, 31)