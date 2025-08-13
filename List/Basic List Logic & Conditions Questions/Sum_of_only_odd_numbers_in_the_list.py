# Sum of only odd numbers in the list.
# Input: [1, 2, 3, 4, 5] → Output: 9
l = [1,2,3,4,5]
sum_odd = 0
odd_n = []
for i in l:
    if i % 2 != 0:
        sum_odd += i
        odd_n.append(i)
print(sum_odd)
print(odd_n)
        
