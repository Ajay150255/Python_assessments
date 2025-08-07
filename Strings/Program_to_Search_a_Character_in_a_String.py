# Input: s = "geeksforgeeks", ch = 'k'
# Output: 3
# Explanation: The character 'k' is present at index 3 and 11 in "geeksforgeeks", but it first appears at index 3.
s = "geeksforgeeks"
ch = "k"
for i in range(len(s)):
    if s[i] in ch:
        print(i)

# Input: s = "geeksforgeeks", ch = 'z'
# Output: -1
# Explanation: The character 'z' is not present in "geeksforgeeks"
s = "geeksforgeeks" 
ch = 'z'
if ch not in s:
    print('-1')
