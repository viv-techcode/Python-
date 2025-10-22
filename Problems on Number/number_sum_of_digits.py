#  Sum of digits of a number

print(" Sum of digits")
n = 9876
print("Number:", n)
s = 0
t = n
while t>0:
    s += t%10
    t//=10
print("Sum digits:", s)

# Output: Sum of digits (1234): 10