#  Check if a Number is Automorphic (square ends with the number)


print(" Automorphic check")
n = 25
print("Number:", n)
sq = n*n
s = str(sq)
ns = str(n)
print("Is automorphic?", s.endswith(ns))	


# Output: 25 is Automorphic  (since 25²=625 ends with 25)