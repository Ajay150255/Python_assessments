#Swap keys and values in dictionary.
d = {'a': 1, 'b': 2, 'c': 3}
swap = {}
for k,v in d.items():
    swap[v] = k
print(swap)
