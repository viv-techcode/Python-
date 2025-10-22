
print("Find largest word in string")

s = "I love programming"
words = s.split()
largest = max(words, key=len)

print("Largest Word:", largest)

# Output: programming