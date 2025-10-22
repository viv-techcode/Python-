import fnmatch
print("Wildcard matching")
text = "hello"
pattern = "h*o"
print("Match?", fnmatch.fnmatch(text, pattern))
# Output: True