#  Program to find sum of GP Series


print(" Sum of GP (integer example) a=3,r=2,n=4")
a = 3; r = 2; n = 4
print("a,r,n:", a,r,n)
# sum = a*(r**n -1)//(r-1) if r !=1
gp_sum = a*(r**n - 1)//(r - 1) if r != 1 else a*n
print("GP Sum:", gp_sum)


# Output: Sum of GP (a=2, r=2, n=4): 30