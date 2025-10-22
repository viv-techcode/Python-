
#  Prime numbers in a given range

print(" Primes in range 1..50")
primes = []
for num in range(2,51):
    is_p = True
    i = 2
    while i*i <= num:
        if num % i == 0:
            is_p = False
            break
        i += 1
    if is_p:
        primes.append(num)
print("Primes:", primes)
	
# Output: Primes from 1–20: [2,3,5,7,11,13,17,19]