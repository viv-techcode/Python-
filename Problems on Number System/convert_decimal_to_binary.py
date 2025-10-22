	
#  Decimal to Binary conversion


print(" Decimal to Binary")

n = 45
print("Decimal:", n)
if n == 0:
    bin_s = "0"
else:
    bin_s = ""
    t = n
    while t>0:
        bin_s = str(t%2) + bin_s
        t//=2
print("Binary:", bin_s)



# Output: Decimal 10 → Binary 1010