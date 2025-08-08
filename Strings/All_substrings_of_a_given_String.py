# Input :  s = "abc"
# Output :  "a", "ab", "abc", "b", "bc", "c"
s = "abc"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])

# Input :  s = "ab"
# Output :  "a",  "ab",  "b"
s = "ab"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])

# Input :  s = "a"
# Output :  "a"
s = 'a'
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
