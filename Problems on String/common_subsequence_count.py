print("Count common characters (simple version)")
s1, s2 = "abc", "bcd"
count = len(set(s1) & set(s2))
print("Common characters:", count)
# Output: 2