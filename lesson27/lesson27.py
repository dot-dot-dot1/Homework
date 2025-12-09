# Lesson 27
def alpha_sorting(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0
    text_lowered = text.lower()
    
    while i < len(abc):
        current_letter = abc[i]
        if current_letter in text_lowered:
            letter_count = text_lowered.count(current_letter)
            result += current_letter * letter_count
        i += 1
    return result
