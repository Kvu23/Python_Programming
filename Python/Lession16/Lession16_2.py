#mist various methods of list
my_list = [1, 2, 3, 4, 5]
print("my_list is ", my_list)

#append methods add element at the end of the list
my_list.append(6)
print("my_list after append is ", my_list)

#insert methods element at mentioned index
my_list.insert(2, 10)
print("my_list after insert is ", my_list)

#remove method remove element from lists
my_list.remove(3)
print("my_list after remove is ", my_list)

#pop method will remove the last element of the list
my_list.pop()
print("my_list after pop is ", my_list)

#reverse method will reverse the list
my_list.reverse()
print("my_list after reverse is ", my_list)

#clear method clear and empty lists
my_list.clear()
print("my_list after clear is ", my_list)

#sort methods will sort the list in ascending order
my_list = [5, 2, 9, 1, 7]
my_list.sort()
print("my_list after sort is ", my_list)


#example of list comprehension  in python this will create a list of squares of numbers from 1 to 10 and those will prints
squares = [x**2 for x in range(1, 11)]
print("squares of numbers from 1 to 10 are ", squares)

