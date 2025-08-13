# Print all numbers divisible by both 2 and 3.
# Input: [6, 9, 12, 14] → Output: [6, 12]
l = [6,9,12,14]
out = []
for i in l:
    if i % 2 == 0 and i % 3 == 0:
        out.append(i)
print(out)
