print("Remove brackets from expression")
expr = "(a+b)*(c-d)"
result = ''.join([ch for ch in expr if ch not in '(){}[]'])
print("Result:", result)
# Output: a+b*c-d