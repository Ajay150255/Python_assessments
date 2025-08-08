# Input: s1 = “geeks”  s2 = “kseeg”
# Output: true
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.
s1 = "geeks"  
s2 = "kseeg"
if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq1 = {}
    freq2 = {}
    
    for i in s1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1
    print(freq1)
    
    for i in s2:
        if i in freq2:
            freq2[i] += 1
        else:
            freq2[i] = 1
    print(freq2)
if freq1 == freq2:
    print("yes")
else:
    print("no")

# Input: s1 = "allergy", s2 = "allergyy"
# Output: false
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.
s1 = "allergy"
s2 = "allergyy"
if len(s1) != len(s2):
    print("Not anagrams")
else:
    freq1= {}
    freq2 = {}
    

# Input: s1 = "allergy", s2 = "allergyy"
# Output: false
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.
s1 = "listen"
s2 = "lists"
if len(s1) != len(s2):
    print("Not anagrams")
else:
    freq1= {}
    freq2 = {}
    
