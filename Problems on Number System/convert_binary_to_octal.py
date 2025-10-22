

# Convert binary to octal


print(" Binary to Octal (via decimal)")
bin_str = "1101011"
print("Binary:", bin_str)
# binary -> decimal
dec = 0
i = 0
for ch in bin_str[::-1]:
    if ch == '1':
        dec += 2**i
    i += 1
# decimal -> octal
octal = ""
if dec == 0:
    octal = "0"
else:
    while dec > 0:
        octal = str(dec % 8) + octal
        dec //= 8
print("Octal:", octal)


# Output: Binary 1010 → Octal 12