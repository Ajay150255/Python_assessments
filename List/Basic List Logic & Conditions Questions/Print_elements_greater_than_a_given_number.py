# Print elements greater than a given number.
# Input: arr = [10, 3, 8, 15], n = 5 → Output: [10, 8, 15]
l = [10,3,8,15]
n = 5
new =[]
for i in l:
    if i > 5:
        new.append(i)
print(new)
