# Find all duplicates in a list.
# Input: [1, 2, 2, 3, 4, 4] → Output: [2, 4]
l = [1,2,2,3,4,4]
out  = []
for i in l:
    if l.count(i) > 1 and i not in out:
        out.append(i)
print(out)

##without count
l = [1,2,2,3,4,4]
original = []
dupli = []
for i in l:
    if i in original and i not in dupli:
        dupli.append(i)
    else:
        original.append(i)
print(dupli)
print(original)

