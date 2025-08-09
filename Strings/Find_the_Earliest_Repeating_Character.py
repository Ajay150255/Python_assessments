# Input: s = "geeksforgeeks" 
# Output: e 
# Explanation: e is the first element that repeats
s = "geeksforgeeks"
li_map = []

for ch in s:
    if ch in li_map:
        print("First duplicate char is", ch)
        break
    else:
        li_map.append(ch)


