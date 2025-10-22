print("Character frequency")
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
# Output: {'b':1,'a':3,'n':2}