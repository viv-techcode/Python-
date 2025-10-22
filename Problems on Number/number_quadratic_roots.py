

#  Program to find roots of a Quadratic Equation (ax^2 + bx + c = 0)


print(" Roots of quadratic ax^2+bx+c")
a,b,c = 1, -3, 2  # roots 1 and 2
print("Coefficients:", a,b,c)
disc = b*b - 4*a*c
if disc < 0:
    print("Complex roots (not computing here).")
else:
    root1 = (-b + disc**0.5)/(2*a)
    root2 = (-b - disc**0.5)/(2*a)
    print("Roots:", root1, root2)

# Output: Roots of x² - 3x + 2 = (2.0, 1.0)