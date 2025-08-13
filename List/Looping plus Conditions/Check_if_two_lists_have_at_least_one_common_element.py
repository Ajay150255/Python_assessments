# Check if two lists have at least one common element.
# Input: a = [1, 2, 3], b = [4, 2, 6] → Output: True
a = [1,2,3]
b = [4,2,6]
is_match =  False
for i in a:
    for j in b:
        if i == j:
            is_match = True
            break
print(is_match)

# Take user input for two lists
a = list(map(int, input("Enter first list numbers separated by space: ").split()))
b = list(map(int, input("Enter second list numbers separated by space: ").split()))

# Check for common element
is_match = False
for i in a:
    if i in b:
        is_match = True
        break

print("Do they have a common element? ->", is_match)
