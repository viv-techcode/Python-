#  Print Fibonacci upto Nth Term

print(" Fibonacci upto Nth")
N = 8
print("N:", N)
a,b = 0,1
fib = []
i = 0
while i < N:
    fib.append(a)
    a,b = b,a+b
    i += 1
print("Fib sequence:", fib)	


# Output: Fibonacci up to 7 terms: [0,1,1,2,3,5,8]