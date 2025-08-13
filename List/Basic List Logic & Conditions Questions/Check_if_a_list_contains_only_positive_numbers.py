# Check if a list contains only positive numbers.
# Input: [1, 3, 5, 7] → Output: True
#### Take input from user as space-separated numbers
li = list(map(int, input("Enter numbers separated by space: ").split()))


li = [1,3,5,7]
is_postive = True
for i in li:
  if i < 0:
    is_postive = False
print(is_postive)
