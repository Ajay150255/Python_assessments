# Input : str = geeksforgeeks, k = 3
# Output : r
# Explanation: First non-repeating character is f, second is o and third is r.

# Input : str = geeksforgeeks, k = 2
# Output : o

# Input : str = geeksforgeeks, k = 4
# Output : Less than k non-repeating characters in input.
s = "geeksforgeeks"
freq = {}
k = 4
count = 0
for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
print("freq :", freq)

for i in s:
    print(i)
    if freq[i] == 1:
        count += 1
        if count == k:
            print("Non-repeating char is:", i)
            break
else:
    print("Less than k non-repeating characters in input.")
