#problem 1: print first and last character of string
# name = 'Kaushik chauhan'
# print(name[0])
# print(name[-1])
# print("Length of string is:- ",len(name))

# str1 = "Hello"
# str2 = "World"
# print(str1 + " " + str2)

#problem 2: print characters from index 0 to 6, -7 to -2, 0 to end with step 2 and in reverse order
# text = "Python Programming"
# print(text[0:7]) # prints characters from index 0 to 6
# print(text[-7:-1:1]) # prints characters from index -7 to -2
# print(text[0:len(text):2]) # prints characters from index 0 to end with step 2
# print(text[::-1]) # prints characters in reverse order

#problem 3: print the string in uppercase and lowercase and remove spaces from the string
# text = "  i love python programming  "
# print(text.strip()) # removes spaces from the string
# print(text.title()) # prints the string in title case
# print("number of occurance of o is: ",text.count("o")) # counts the number of occurrences of 'o' in the string

# text = '123abc'
# print(text.isalnum()) # checks if the string contains only alphanumeric characters

#problem 4: print the string mehtods available for string objects
# name = 'John'
# age = 25

# print('My name is {} and I am {} years old.'.format(name, age))
# print(f'My name is {name} and I am {age} years old.')

#problem 5: string manipulations
sentence = "Coding in Python is fun"
# print(sentence)
# print(sentence.replace("fun", "awesome")) # replaces 'fun' with 'awesome'

# print(sentence.find("Python")) # returns the index of the first occurrence of 'Python' 

# print(sentence.upper()) # converts the string to uppercase
vowel = "aeiou"
print(sentence.count(vowel[0])) # counts the number of occurrences of 'a' in the string
print(sentence.count(vowel[1])) # counts the number of occurrences of 'e' in the string
print(sentence.count(vowel[2])) # counts the number of occurrences of 'i' in the string
print(sentence.count(vowel[3])) # counts the number of occurrences of 'o' in the string
print(sentence.count(vowel[4])) # counts the number of occurrences of 'u' in the string

