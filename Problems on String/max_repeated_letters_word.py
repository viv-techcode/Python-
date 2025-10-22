
print("Word with highest repeated letters")


s = "apple banana cherry"
words = s.split()
max_word = max(words, key=lambda w: max(w.count(ch) for ch in set(w)))

print("Result:", max_word)

# Output: apple