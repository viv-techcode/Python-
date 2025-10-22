print("Capitalize first and last letters")
s = "hello world"
words = s.split()
result = ' '.join([w[0].upper() + w[1:-1] + w[-1].upper() if len(w)>1 else w.upper() for w in words])
print("Result:", result)
# Output: HellO WorlD