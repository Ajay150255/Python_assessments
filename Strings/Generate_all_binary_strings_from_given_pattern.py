# Input: str = "1??0?101"
# Output: 
# 10000101
# 10001101
# 10100101
# 10101101
# 11000101
# 11001101
# 11100101
# 11101101
s = "1??0?101"
res = [s]   # Start with original string in a list

# Repeat for each '?' in the original string
for _ in range(s.count('?')):
    print(_)
    temp = []   # Store new strings after replacing one '?'
    for pattern in res:
        temp.append(pattern.replace('?', '0', 1))  # Replace first '?' with '0'
        temp.append(pattern.replace('?', '1', 1))  # Replace first '?' with '1'
    res = temp  # Move to next set of strings

print(res)
    
