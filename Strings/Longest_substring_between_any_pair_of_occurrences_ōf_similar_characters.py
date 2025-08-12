# Input: s = "accabbacc"
# Output: 6
# Explanation: The matching characters are 'c' at positions 1 and 8. Substring between them is "cabbac", of length 6.
s = "accabbacc"
first_index = {}
max_len = 0

for i in range(len(s)):  # loop over index numbers
    print("i", i)
    ch = s[i]
    if ch not in first_index:
        first_index[ch] = i  # store first index
    else:
        length = i - first_index[ch] - 1  # gap between same chars
        if length > max_len:
            max_len = length

print(max_len)  # 6

# Input: s = "aa"
# Output: 0
# Explanation: Matching characters 'a' are at positions 0 and 1. No characters in between, so length is 0.
s = 'aa'
index = {}
max_len = 0
for i in range(len(s)):
    print("i", i)
    ch = s[i]
    if ch not in index:
        index[ch] = i
        print ("index", index)
    else:
        length = i - index[ch] - 1
        if length > max_len:
            max_len  = length
print("max_len", max_len)


# Input: s = "abcd"
# Output: -1
# Explanation: No repeated characters exist, hence no valid substring between same characters.
s1 = "abcd"
index = {}
max_len = -1
for i in range(len(s1)):
    ch = s1[i]
    if ch not in index:
        index[ch] = i
    else:
        length = i - index[ch] - 1
        if length > max_len:
            max_len = length
print("max_len", max_len)












    
    
    
