print('Dictionary coding Q & A')
# Q1. Count frequency of each key in a dictionary
d = {'a': 2, 'b': 3, 'a': 5, 'c': 2}
freq  = {}
for k in d.keys():
    if k in freq:
        freq[k] += 1
    else:
        freq[k] = 1
print(freq)

#Q2. Count frequency of each value in a dictionary
d = {"a": 2, "b": 3, "c": 2, "d": 3, "e": 1}
freq = {}
for v in d.values():
    if v in freq:
        freq[v] += 1
    else:
        freq[v] = 1
print(freq)

#Q3. Count frequency of characters from a string and store in dictionary
s = "programming"
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#Q4. Count frequency of numbers from a list and store in dictionary
nums = [4, 5, 6, 7, 5, 9, 4, 10, 6, 5]
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#Q5. Count frequency of words in a sentence
s = "python is easy and python is powerful"
s1 = s.split()
freq = {}
for i in s1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#Find the most frequent value in a dictionary (output = 2 or 3)
d = {'a': 2, 'b': 1, 'c': 2, 'd': 3, 'e': 3}
freq = {}
for v in d.values():
    if v in freq:
        freq[v] += 1
    else:
        freq[v] = 1
print(freq)

max_count = max(freq.values())

most_freq = []
for k, v in freq.items():
    if v == max_count:
        most_freq.append(k)
print(most_freq)

#Count frequency of first letters of keys
d = {'apple': 5, 'ant': 3, 'banana': 2, 'ball': 4, 'cat': 1}
freq = {}

for k in d.keys():
    # print("k", k)
    first = k[0]
    # print("first", first)
    if first in freq:
        freq[first] += 1
    else:
        freq[first] = 1
print(freq)

#Count frequency of lengths of keys
d = {'pen': 10, 'book': 5, 'copy': 2, 'laptop': 7, 'tv': 1}
freq = {}
for k in d.keys():
    lengths = len(k)
    if lengths in freq:
        freq[lengths] += 1
    else:
        freq[lengths] = 1
print(freq)

#Count frequency of even vs odd values
d = {'a': 2, 'b': 5, 'c': 6, 'd': 9, 'e': 10}
freq = {'even' : 0, 'odd' : 0}

for v in d.values():
    if v % 2 == 0:
        freq['even'] += 1
    else:
        freq['odd'] += 1
print(freq)

#Find the sum of all values in a dictionary
d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
total = 0
for v in d.values():
    total += v
print(total)

#Find the key with the maximum value
d = {'apple': 50, 'banana': 20, 'cherry': 75, 'date': 40}
max_key = 0
max_value = 0

for k, v in d.items():
    if v > max_value:
        max_value = v
        max_key = k
print(max_key,max_value)

#Find the key with the minimum value
d = {'x': 15, 'y': 5, 'z': 25, 'w': 10}

min_key = None
min_value = float('inf')

for k, v in d.items():
    if v < min_value:
        min_value = v
        min_key = k
print(min_key,":",min_value)

#Find average of dictionary values
d = {'a': 10, 'b': 30, 'c': 50, 'd': 20}

total = 0
count = 0
for v in d.values():
    total += v
    count += 1
    
avg = total / count
print('avg', avg)

#Find the product of all values in a dictionary
d = {'a': 2, 'b': 3, 'c': 4}

product = 1
for v in d.values():
    product *= v
print(product)

#Extract keys whose values are even numbers
d = {'a': 10, 'b': 15, 'c': 20, 'd': 25}

output = []
for k, v in d.items():
    if v % 2 == 0:
        output.append((k, v))
print(dict(output))

# Extract keys with length greater than 3
d = {'apple': 50, 'bat': 20, 'cherry': 75, 'dog': 40}
output = []
for k in d.keys():
    if len(k) > 3:
        output.append(k)
print(output)

#Sort list in ascending order (without sorted())
l = [5, 3, 8, 6, 2]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)

##Sort list in decending order (without sorted())
l = [5, 3, 8, 6, 2]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]
print(l)

#Merge two lists into one
l1 = [1, 2, 3]
l2 = [4, 5, 6]
merge = []

for i in l1:
    # merge.append(i)
    merge += [i]
    
for i in l2:
    merge += [i]
print(merge)
    
#Find common elements in two lists
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
common = []

for i in l1:
    for j in l2:
        if i == j:
            common += [i]
        
print(common)

#Find elements present in first list but not in second
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7]
diff = []

for x in l1:
    if x not in l2:
        diff += [x]
print(diff)

#Count frequency of each element in a list
l = [1, 2, 2, 3, 3, 3]
freq = {}
for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

list_item = []
for k, v in freq.items():
    list_item.append([k,v])
print(list_item)

#Remove duplicates from a list
l = [5, 3, 4, 2, 3, 6, 5]
l_dup = []
l_dupli = []

for i in l:
    if i not in l_dup:
        l_dup += [i]
print(l_dup)

# Find first duplicate element
l = [5, 3, 4, 2, 3, 6, 5]

seen = []
first_duplicate = None

for i in l:
    if i in seen:   # check in list
        first_duplicate = i
        break
    else:
        seen.append(i)

print(first_duplicate)
print(seen)

#Check if a list is a sublist of another
l1 = [1, 2, 3, 4, 5]
sub = [2, 3, 4]

found = all(i in l1 for i in sub)
print(found)

# Reverse a string without using slicing.
# Input: "hello" → Output: "olleh"
s = "hello"
s1 = ""
for i in s:
    s1 = i + s1
print(s1)

# Count vowels and consonants in a string.
# Input: "Python" → Output: Vowels=1, Consonants=5
s = "Python"
vowels = "aeiouAEIOU"
count_vo = 0
count_con = 0
for i in s:
    if i in vowels:
        count_vo += 1
    if i not in vowels:
        count_con += 1
print(count_vo)
print(count_con)

# Check if a string is a palindrome.
# Input: "madam" → Output: True
s0 = "madam"
rev = ""
for i in s0:
    rev = i + rev
print(rev)
is_plain = False
if s0 == rev:
    is_plain = True
print(is_plain)

s = "programming"

# Step 1: Count frequencies manually
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq)

# Step 2: Collect non-repeating chars
non_repeats = []
for ch in s:
    if freq[ch] == 1:
        non_repeats.append(ch)
print(non_repeats)

# Step 3: Print 1st, 2nd, 3rd non-repeating
if len(non_repeats) >= 1:
    print("non-repeating chars are:", non_repeats[0], non_repeats[1], non_repeats[2], non_repeats[3])
    
# Remove all duplicate characters from a string.
# Input: "programming" → Output: "progamin"
s= "programming"
dup = ''
dup1 = ''
for i in s:
    if i not in dup:
        dup += i
    else:
        dup1 += i
print(dup)
print(dup1)

# Find the second largest number in a list without using max() or sorted().
# Input: [10, 20, 4, 45, 99] → Output: 45
l = [-10, -20, -4, -45, 99]
print(sorted(l)) ### assending order

max = l[0]      # assume first element
seco = float('-inf')  # very small

for i in l:
    if i > max:
        seco = max
        max = i
    elif i > seco and i != max:
        seco = i

print("Largest:", max)
print("Second Largest:", seco)

# Remove duplicates from a list without using set().
# Input: [1,2,2,3,4,4,5] → Output: [1,2,3,4,5]
l = [1,2,2,3,4,4,5]
l_dup = []
for i in l:
    if i not in l_dup:
        # l_dup.append
        l_dup += [i]
print(l_dup)

l = [1, 2, 3, 4, 5, 6]
k = 2
n = len(l)
rotated = []  

for i in range(n):
    new_index = (i + k) % n   # shift each element k places
    rotated.append(l[new_index])

print(rotated)











