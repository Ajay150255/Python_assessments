# Find the second largest number (without inbuilt functions).
# Input: [3, 5, 1, 8, 7] → Output: 7
l = [3, 5, 1, 8, 7]

# Step 1: Find the largest
largest = l[0]
for num in l:
    if num > largest:
        largest = num
print(largest)

# Step 2: Find the second largest
second_largest = l[0]
for num in l:
    if num > second_largest and num < largest:
        second_largest = num

print(second_largest)  # Output: 7

#step 3 : thrid largest
third_largest = l[0]
for num in l:
    if num > third_largest and num < second_largest:
        third_largest = num
print(third_largest)




