# Input : "This is a test string"
# Output : Minimum length word: a
#          Maximum length word: stringA
s = "GeeksforGeeks A computer Science portal for Geeks" 
print(s.lower())
print(s.upper())
words = s.split()

min_word = words[0]
max_word = words[0]

for w in words:
    if len(w) > len(max_word):
        max_word = w
    elif len(w) < len(min_word):
        min_word = w

print("Minimum length word:", min_word)
print("Maximum length word:", max_word)

        

