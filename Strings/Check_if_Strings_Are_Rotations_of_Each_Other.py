# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: After 2 right rotations, s1 will become equal to s2.
s1 = "abcd"
s2 = "cdab"
s3 = s1 + s1
print(s3)
if s2 in s3:
    print("True")
else:
    print("False")


# Input: s1 = "aab", s2 = "aba"
# Output: true
# Explanation: After 1 left rotation, s1 will become equal to s2.
s1 = "aab"
s2 = "aba"
s3 = s1 + s1
print(s3)
if s2 in s3:
    print("True")
else:
    print("False")

# Input: s1 = "abcd", s2 = "acbd"
# Output: false
# Explanation: Strings are not rotations of each other.
s1 = "abcd"
s2 = "acbd"
s3 = s1 + s1
print(s3)
if s2 in s3:
    print("True")
else:
    print("False")
