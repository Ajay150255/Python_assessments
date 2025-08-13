# Check if a list is strictly increasing.
# Input: [1, 3, 5, 7] → Output: True
l = [1,0,5,7]
out = True
for i in range(len(l) - 1):
    print("i", i)
    if l[i] > l[i+1]:
        out = False
        break
print(out)
