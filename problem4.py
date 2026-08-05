#Problem #4
#Letter used counter (EXCLUDING special characters)

import string
alphabet = string.ascii_lowercase

text = str(input("Enter a sentence: "))

counts = {}

for char in text:
    
    if 'A' <= char <= 'Z':
        clean_char = chr(ord(char) + 32)
    else:
        clean_char = char
    
    if clean_char in alphabet:
        counts[clean_char] = counts.get(clean_char, 0) + 1

for letter in sorted(counts.keys()):
    print(f"{letter}: {counts[letter]}")
