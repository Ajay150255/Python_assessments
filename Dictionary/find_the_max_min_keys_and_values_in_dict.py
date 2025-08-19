#find the max, min keys and values in dict
d = {'a':10, 'b':15, 'c':20}
max_key, max_value = None, float('-inf')
min_key, min_value = None, float('inf')

for k, v in d.items():
    if v > max_value:
        max_key, max_value = k, v
    if v < min_value:
        min_key, min_value = k, v
        
print(max_key, ':', max_value)
print(min_key, ':', min_value)
