# program to understand escape sequence

str1 = "this is a sample string \t we are creating it in the python"
print(str1)

# string concatenations

str1 = "kaushik "
len1 = len(str1)
print("len1 = ",len1)
str2 = "chauhan"
len2 = len(str2)
print("len2 = ",len2)

print(str1 + str2)
print("Final string length",len(str1 + str2))

#indexing example in string
str = "Kaushik Chauhan"
print(str[0:7]) #positive index starts from 0 to 7
print(str[-7:-1]) # negative index starts from the last word onwards

#slicing examples
print(str[-7:len(str)]) #-7 to length of string



