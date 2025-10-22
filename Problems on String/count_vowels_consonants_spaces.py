print("Count vowels, consonants, spaces")
s = "Hello World"
vowels = "aeiouAEIOU"
v = c = sp = 0
for ch in s:
    if ch in vowels:
        v += 1
    elif ch == ' ':
        sp += 1
    elif ch.isalpha():
        c += 1
print("Vowels:", v, "Consonants:", c, "Spaces:", sp)
# Output: Vowels: 3 Consonants: 7 Spaces: 1