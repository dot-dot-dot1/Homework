# Lesson 31
# Creating functions that can take two strings and determine if they are __[anagrams](https://en.wikipedia.org/wiki/Anagram)__ of each other.

# ### You will learn:

# - Two different ways to determine anagrams

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word1 = word1.replace(" ", "").lower()
word2 = word2.replace(" ", "").lower()
if sorted(word1) == sorted(word2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")
