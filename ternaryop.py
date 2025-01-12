vowel="aeiou"
word=input("enter the word: ")
vo="vowel" if any(char in vowel for char in word ) else "not vowel"
print(vo)