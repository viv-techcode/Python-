print("Remove non-alphabetic characters")
s = "He!!o Wo123rld"
result = ''.join([ch for ch in s if ch.isalpha()])
print("Result:", result)
# Output: HeoWorld