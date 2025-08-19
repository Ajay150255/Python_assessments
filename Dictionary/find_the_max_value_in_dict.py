#find the max value in dict.
d = {'a':10, 'b':15, 'c':20}

max_val = float('-inf')  # smallest possible
min_val = float('inf')   # largest possible

for v in d.values():
    if v > max_val:
        max_val = v
    if v < min_val:
        min_val = v
        
print(max_val)
print(min_val)
