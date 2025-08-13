# Separate even and odd numbers into two lists.
# Input: [1, 2, 3, 4, 5] → Output: Even: [2, 4], Odd: [1, 3, 5]
l = [1,2,3,4,5]
even = []
odd = []
for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
