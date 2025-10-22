
#  Maximum and Minimum digit in a number


print(" Max and Min digit")
n = 70932
print("Number:", n)
t = n
maxd = -1
mind = 10
while t>0:
    d = t%10
    if d > maxd: maxd = d
    if d < mind: mind = d
    t//=10

print("Max digit:", maxd, "Min digit:", mind)


# Output: Max digit: 9, Min digit: 1

