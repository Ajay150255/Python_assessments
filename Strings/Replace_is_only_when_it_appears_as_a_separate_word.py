s = "This island is beautiful"
s1 = s.split()
print(s1)
rev =''

for i in s1:
    if i == 'is':
        rev += 'was '
    else:
        rev += i + " "
print(rev)
