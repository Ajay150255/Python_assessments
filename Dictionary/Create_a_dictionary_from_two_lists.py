# Create a dictionary from two lists (keys & values).
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)

d  = {}
for i in range(len(keys)):
    print(i)
    d[keys[i]] = values[i]
print(d)
