# Remove all negative numbers from a list.
# Input: [1, -3, 5, -2, 6] → Output: [1, 5, 6]
l = [1, -3, 5, -2, 6]
num = []
for i in l:
    if i > 0:
        num.append(i)
print(num)
