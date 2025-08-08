# Input : s = "abcde",  pos = 1
# Output : s = "acde"

s = "abcde"
pos = 1
new_s= ''
for i in range(len(s)):
    if i != pos:
        new_s += s[i]
print(new_s)

# Input : s = "a",  pos = 0
# Output : s = ""
s = "a"
pos = 0
new_s = ""
for i in range(len(s)):
    if i != pos:
        new_s += s[i]
print(new_s)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
