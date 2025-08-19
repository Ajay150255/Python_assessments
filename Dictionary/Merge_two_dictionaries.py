# Merge two dictionaries.
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
merge = {}
for k,v in d1.items():
    merge[k] = v
for k, v in d2.items():
    merge[k] = v
print(merge)
