#  LCM of two numbers

print(" LCM")
a = 12; b = 15
print("a,b:", a,b)
# lcm = abs(a*b)//gcd
# reuse gcd calc
x,y = a,b
while y:
    x,y = y, x%y
g = x
lcm = (a*b)//g
print("LCM:", lcm)	


# Output: LCM of (4, 6): 12