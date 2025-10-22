

#  Convert Binary to Decimal


print(" Binary to Decimal")
bin_str = "1101"
print("Binary:", bin_str)
dec = 0
i = 0
for ch in bin_str[::-1]:
    if ch == '1':
        dec += 2**i
    i += 1
print("Decimal:", dec)


# Output: Binary 1011 → Decimal 11