# Input: s = "abba"
# Output: 1
# Explanation: s is a palindrome
s = "abba"
s1 = ""
for i in s:
    s1 = i + s1
print(s1)

print(int(s == s1))

# Input: s = "abc" 
# Output: 0
# Explanation: s is not a palindrome
s = "abc"
s1 = ""
for i in s:
    s1 = i + s1
print(s1)
print(int(s==s1))
