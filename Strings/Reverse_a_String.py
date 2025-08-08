# Input: s = "GeeksforGeeks"
# Output: "skeeGrofskeeG"
# Explanation : The first character G moves to last position, the second character e moves to second-last and so on.
s = "GeeksforGeeks"
rev_s = ""
for i in s:
    print(i)
    if i != rev_s:
        rev_s = i + rev_s
print(rev_s)


# Input: s = "abdcfe"
# Output: "efcdba"
# Explanation: The first character a moves to last position, the second character b moves to second-last and so on. 
s = "abdcfe"
rev_s = ""
for i in s:
    if i != rev_s:
        rev_s = i + rev_s
print(rev_s)
        




