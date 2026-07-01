#this programs shows how to create a lists

marks = [45, 67, 89, 90, 78]
print("marks are ", marks)

mixed = [45, 67, 89, 90, 78.5, "hello", True]
print("mixed list is ", mixed) 

empty = []
print("empty list is ", empty)

#access lists elements using index
print("first element of marks is ", marks[0])
print("second element of marks is ", marks[1])
print("third element of marks is ", marks[2])
print("fourth element of marks is ", marks[3])
print("fifth element of marks is ", marks[4])

print("last element of mixed is ", mixed[-1])
print("second last element of mixed is ", mixed[-2])
print("third last element of mixed is ", mixed[-3])
print("fourth last element of mixed is ", mixed[-4])
print("fifth last element of mixed is ", mixed[-5])


print(marks[2:4])
print(mixed[-1:-4:-1])
