#  Check if a number is a strong number or not (sum of factorials of digits equals number)


print(" Strong number check")
n = 145
print("Number:", n)
def factorial(x):
    res = 1
    i = 1
    while i <= x:
        res *= i
        i+=1
    return res
t = n
s = 0
while t>0:
    d = t%10
    s += factorial(d)
    t//=10
print("Is strong number?", s == n)


# Output: 145 is Strong