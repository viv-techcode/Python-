pairs = [(1, 2), (3, 4), (5, 9), (2, 1), (4, 3)]
symmetric = []
for (a, b) in pairs:
    if (b, a) in pairs and (b, a) not in symmetric:
        symmetric.append((a, b))
print("Symmetric pairs:", symmetric)
	

# Output: Symmetric pairs: [(1, 2), (3, 4)]