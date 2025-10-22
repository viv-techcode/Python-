#  Replace all 0s with 1s in a given integer

print(" Replace 0s with 1s in integer")
n = 102040
print("Number:", n)
res = 0
mul = 1
t = n
if t == 0:
    res = 1
else:
    while t>0:
        d = t%10
        if d == 0:
            d = 1
        res += d * mul
        mul *= 10
        t//=10
print("Result:", res)



# Output: 102030 → 112131

