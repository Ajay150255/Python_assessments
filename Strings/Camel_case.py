# Input: "i got intern at geeksforgeeks"
# Output: "iGotInternAtGeeksforgeeks"
s = "i got intern at geeksforgeeks"
s1= s.split()
camel_s = s1[0].lower()
for i in s1[1:]:
    camel_s += i.capitalize()
print(camel_s)
    
# Input: "here comes the garden"
# Output: "hereComesTheGarden"
s = "here comes the garden"
s1 = s.split()
print(s1)
camel_s = s1[0].lower()
for i in s1[1:]:
    camel_s += i.capitalize()
print(camel_s)

