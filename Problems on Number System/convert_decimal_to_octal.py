

#  Convert decimal to octal


print(" Decimal to Octal")
n = 100
print("Decimal:", n)
if n == 0:
    oct_s = "0"
else:
    oct_s = ""
    t = n
    while t>0:
        oct_s = str(t%8) + oct_s
        t//=8
print("Octal:", oct_s)


# Output: Decimal 10 → Octal 12