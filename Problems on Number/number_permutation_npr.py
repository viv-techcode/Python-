#  Permutations in which N people can occupy R seats (nPr)


print(" Permutations nPr")
n = 5; r = 3
print("n,r:", n,r)
# nPr = n*(n-1)*...*(n-r+1)
res = 1
i = 0
while i < r:
    res *= (n - i)
    i += 1
print("nPr:", res)	

# Output: nPr (5, 2): 20