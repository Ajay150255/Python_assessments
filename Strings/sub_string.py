# Input: txt = "geeksforgeeks", pat = "eks"
# Output: 2
# Explanation: String "eks" is present at index 2 and 9, so 2 is the smallest index.
txt = "geeksforgeeks"
pat = "eks"
if pat in txt:
    print(txt.index(pat))
else:
    print("1")

# Input: txt = "geeksforgeeks", pat = "xyz"
# Output: -1.
# Explanation: There is no occurrence of "xyz" in "geeksforgeeks"
txt = "geeksforgeeks"
pat = "xyz"
if pat in txt:
    print(txt.index(pat))
else:
    print("1")
