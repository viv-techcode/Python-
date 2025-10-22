#  Reverse digits of a number


print(" Reverse digits")
n = 12345
print("Number:", n)
rev = 0
t = n
while t>0:
    rev = rev*10 + t%10
    t//=10
print("Reversed:", rev)	


# Output: Reverse of 12345: 54321