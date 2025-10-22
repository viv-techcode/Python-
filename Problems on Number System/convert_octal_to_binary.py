

#  Convert octal to binary

print(" Octal to Binary (via decimal)")
oct_s = "157"
print("Octal:", oct_s)
# octal -> decimal
dec = 0
i = 0
for ch in oct_s[::-1]:
    dec += int(ch) * (8**i)
    i += 1
# decimal -> binary
bin_s = ""
if dec == 0:
    bin_s = "0"
else:
    t = dec
    while t>0:
        bin_s = str(t%2) + bin_s
        t//=2
print("Binary:", bin_s)
	
# Output: Octal 12 → Binary 1010
