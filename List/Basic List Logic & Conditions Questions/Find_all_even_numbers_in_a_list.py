# Find all even numbers in a list.
# Input: [2, 5, 6, 7, 8] → Output: [2, 6, 8]

l = [2,5,6,7,8]
even = []
for i in l:
    if i % 2 == 0:
        even.append(i)
print(even)
