# Count how many times a specific number appears.
# Input: nums = [1, 2, 3, 2, 2], x = 2 → Output: 3
l = [1,2,3,4,2,2]
x = 2
count = 0
for i in l:
    if i == 2:
        count += 1
print(count)
