# Replace all elements > 10 with 10.
# Input: [5, 12, 8, 20] → Output: [5, 10, 8, 10]
l = [5,12,8,20]
for i in range(len(l)):
    if l[i] > 10:
        l[i] = 10
print(l)

out = []
for i in l:
    if i > 10:
        out.append(10)
    else:
        out.append(i)
print(out)
