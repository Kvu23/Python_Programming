# create a lists in the python 
marks = [94.5, 60.5, 75.5, 35.5 , 59.5, 100.0 ]

# print all the marks
print(marks)

# print type of marks
print("type of marks",type(marks))

# print length of lists and individual member of lists
print("length of the lists ",len(marks))
# print("individual marks elements\n\n")
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

#sub lists in th lists
print(marks[1:4])
print(marks[:4])
print(marks[-3:-1])
print(marks[:-2])
print(marks[-6:])
print(marks[-1:])
print(marks[-6:-1])



#in python we can create different data types in the lists together
student = ["Kaushik", 98.5, 36, "Male", "Bengaluru"]
print("typing lists : ",student)
print("Type of student ",type(student))
student[0] = "Heena"
print("Changed list index ",student[0])

#will give error as index out of range
print(student[5])


#strings are the immutable and lists are mutables
str = "Kaushik"
print(str)
# str[0] = "H"








