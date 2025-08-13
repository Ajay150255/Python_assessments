# Sum of numbers at even indexes.
# Input: [10, 20, 30, 40, 50] → Output: 10 + 30 + 50 = 90
l = [10, 20, 30, 40, 50]
total = 0
for i in range(0, len(l), 2):
    print(i)
    print(l[i])
    total += l[i]
print(total)

