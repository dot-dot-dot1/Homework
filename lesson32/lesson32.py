# Lesson 32
# Create a function that takes two string inputs, return a single sorted list of characters that are found in each string.

# ### You will learn:

# - How to use sets to remove duplicates in a string



def common_characters(str1, str2):
  
    set1 = set(str1)
    set2 = set(str2)
    common = set1.intersection(set2)
    return sorted(list(common))
result = common_characters("apple", "grape")
print(result) 
