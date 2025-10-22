#  Greatest of three numbers


print(" Greatest of three numbers")
a=10; b=20; c=30
print(a,b,c,"-> greatest:", a if a>b and a>c else (b if b>c else c))
	
# Output: Greatest of (10, 20, 30): 30