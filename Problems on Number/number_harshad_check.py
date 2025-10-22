#  Check if a number is Harshad number (divisible by sum of digits)


print(" Harshad number check")
n = 18
print("Number:", n)
s = 0
t = n
while t>0:
    s += t%10
    t//=10

print("Is Harshad?", n % s == 0)


# Output: 18 is Harshad 