# Check if a number is armstrong number or not (3-digit definition)


print(" Check Armstrong (3-digit)")
n = 153
print("Number:", n)
temp = n
sum_pow = 0
while temp>0:
    d = temp%10
    sum_pow += d**3
    temp//=10
print("Is Armstrong?", sum_pow == n)
	
# Output: 153 is Armstrong 
