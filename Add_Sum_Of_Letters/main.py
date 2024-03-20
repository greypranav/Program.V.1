lettersum = lambda s: sum(ord(c)-96 for c in s)  
for s in ["", "a", "z", "cab", "excellent", "microspectrophotometries"]:
    print(lettersum(s))