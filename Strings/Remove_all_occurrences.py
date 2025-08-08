# Input : s = "geeksforgeeks"
#         c = 'e'
# Output : s = "gksforgks"
s = "geeksforgeeks"
c = "e"
s1 = ""
for i in s:
    if i != c:
        s1 += i
print(s1)

# Input : s = "geeksforgeeks"
#         c = 'g'
# Output : s = "eeksforeeks"
s = "geeksforgeeks"
c = "g"
s1 = ""
for i in s:
    if i != c:
        s1 += i
print(s1)


# Input : s = "geeksforgeeks"
#         c = 'k'
# Output : s = "geesforgees"
s = "geeksforgeeks"
c = "k"
s1 = ""
for i in s:
    if i != c:
        s1 += i
print(s1)




