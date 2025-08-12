# Input: air
# Output: 3
# Explanation :
# 3 pairs that are equal are (a, a), (i, i) and (r, r)
# Input : geeksforgeeks
# Output : 31
s = "air"
count = 0
for i in range(len(s)):
    print("i", i)
    for j in range(len(s)):
        print("j", j)
        if s[i] == s[j]:
            count += 1
print(count)
        


        

