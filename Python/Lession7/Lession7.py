# various string functions

str = "My name is kaushik chauhan"

#sample exercise with endswith
print(str.endswith("an"))
print(str.endswith("as"))

#function for capitalize

str = "i am studying python from ApnaCollege"
print("example of string capitalize:-\n ",str.capitalize()) # this will create new string

#this will modify the original strings
print(str)
str = str.capitalize()
print(str)

# replace functions
str = 'My name is kaushik chauhan. I am studying python from apna college'
print(str)
print(str.replace("kaushik","Heena"))

#find functions
print("index is:- ",str.find("e"))
print("index is:-", str.find("is"))

#count functions

print("count of e is ",str.count("e"))
print("count of a is ",str.count("a"))
print("count of is is ",str.count("is"))

