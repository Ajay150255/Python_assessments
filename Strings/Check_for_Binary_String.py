# Input: s = "01010101010"
# Output: true
s = "01010101010"
t = True
for i in s:
    if i != "0" and i != "1":
        t = False
print(t)

# Input: s = "geeks101"
# Output: false 
s = "geeks101"
t = True
for i in s:
    if i != "0" and i != "1":
        t = False
print(t)


s = "100101010101010101"
t = True
for i in s:
    if i != "0" and i != "1":
        t = False
print(t)
