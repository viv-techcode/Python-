#  Check if a number is prime or not


print(" Check prime")
n = 17
print("Number:", n)
if n < 2:
    print("Not prime")
else:
    is_prime = True
    i = 2
    while i*i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    print("Is prime?", is_prime)


# Output: 17 is Prime 