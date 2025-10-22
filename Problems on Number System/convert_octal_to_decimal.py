
# Convert octal to decimal

print(" Octal to Decimal")
oct_s = "157"
print("Octal:", oct_s)
dec = 0
i = 0
for ch in oct_s[::-1]:
    dec += int(ch) * (8**i)
    i += 1
print("Decimal:", dec)

# Output: Octal 12 → Decimal 10