# Input: s = "Geeks", c = 'A', pos = 3
# Output: GeeAks
""""Using index method"""
s = "Geeks"
c = "A"
pos = 3
print(s[:pos])
print(s[pos:])
new_string = s[:pos] + c + s[pos:]
print(new_string)

# Input: s = "HelloWorld", c = '!', pos = 5
# Output: Hello!World
""""Using index method"""
s = "HelloWorld"
c = '!'
pos = 5
print(s[:pos])
print(s[pos:])
new_string = s[:pos] + c + s[pos:]
print(new_string)



'''''''using for loop''''''
New_s = ''

for i in range(len(s) + 1):
    if i == pos:
        new_s += c 
    if i < len(s):
        new_s += s[i]

print("Result:", new_s)

