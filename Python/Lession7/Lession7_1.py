name  = 'kaushik chauhan'

#name[0] = 'K'  # This will raise an error because strings are immutable in Python

# #string methods Length
Len = len(name)
print(Len)

# #string methods Convert to uppercase
print(name.upper(), name)

# #string lower method
print(name.lower(), name)

# #string capitalize method
print(name.capitalize(), name)

# #string title methods
print(name.title(), name)

#string strip methods
text = "   kaushik chauhan   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#string find methods
text = 'Python is fun and easy to learn. Python is a popular programming language.'
print(text.find('Python'))  # Output: 0
print(text.find('fun'))     # Output: 10
print(text.find('Java'))    # Output: -1 (not found)

#string replace method
print(text.replace('Python', 'Java'))  # Output: Java is fun and easy to learn. Java is a popular programming language.

#string split method
print(text.split())  # Output: ['Python', 'is', 'fun', 'and', 'easy', 'to', 'learn.', 'Python', 'is', 'a', 'popular', 'programming', 'language.']   


#string join method method with delimiter
print(' '.join(['Apple', 'Bananas', 'Pinapples']))  # Output: Apple Bananas Pinapples

#string is methods
text = 'Kaushik1990'

print(text.isalnum())  # Output: True (contains only alphanumeric characters)
print(text.isalpha())  # Output: False (contains digits)
print(text.isdigit())  # Output: False (contains letters)
print(text.islower())  # Output: False (contains only lowercase letters)
print(text.isupper())  # Output: False (contains only uppercase letters)
print(text.isspace())  # Output: False (contains non-whitespace characters)
