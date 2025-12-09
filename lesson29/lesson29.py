# Lesson 29


def consonant_count(text, vowel=False):
    total = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for character in text.lower():
        if character.isalpha():
            # Count vowels or consonants depending on the flag
            if vowel and character in vowels:
                total += 1
            elif not vowel and character not in vowels:
                total += 1

    return total
user_text = input("Enter a word or sentence: ")
print(f"The number of consonants is {consonant_count(user_text)}")
print(f"The number of vowels is {consonant_count(user_text, vowel=True)}")
