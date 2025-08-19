#Count frequency of elements in a list (store in dict).
# Input: [1,2,2,3,1,4]
# Output: {1:2, 2:2, 3:1, 4:1}
d = [1,2,2,3,1,4]
d_out = {}
for i in d:
    if i in d_out:
        d_out[i] += 1
    else:
        d_out[i] = 1
print(d_out)
