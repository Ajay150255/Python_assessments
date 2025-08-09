# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: 'f' is the first character in the string which does not repeat.
s = "geeksforgeeks"
freq = {}
for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
print(freq)

for i in s:
    if freq[i] == 1:
        print("Non-repeating char is:", i)
        break

# Input: s = "racecar"
# Output: 'e'
# Explanation: 'e' is the only character in the string which does not repeat.
s = "racecar"
freq = {}
for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)

for i in s:
    if freq[i] == 1:
        print("Non-repeating char is:", i)
        break

# Explanation: All the characters in the given string are repeating.
s = "aabbccc"
freq = {}
for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)

for i in s:
    if freq[i] == 1:
        print("Non-repeating char is:", i)
        break
else:
    print("$")







