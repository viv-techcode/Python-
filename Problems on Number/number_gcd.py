#  GCD of two numbers

print(" GCD")
a = 48; b = 18
print("a,b:", a,b)
# Euclid
x,y = a,b
while y:
    x,y = y, x%y
print("GCD:", x)

# Output: GCD of (12, 18): 6