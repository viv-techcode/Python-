#  Check if a number is palindrome or not

print(" Check if number is palindrome")
n = 121
print("Number:", n)
temp = n
rev = 0
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
print("Is palindrome?", rev == n)	


# Output: 121 is Palindrome