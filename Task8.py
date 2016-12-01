def remove_vowel(s):
        if not s:
                return s
        elif s[0].lower() in "aeiou":
                return remove_vowel(s[1:])
        return s[0] + remove_vowel(s[1:])

print("This program removes the vowels from words")
words = input("Input word: ")
print(remove_vowel(words))
