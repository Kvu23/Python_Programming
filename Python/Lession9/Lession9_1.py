# lists various methods

lists = [2,1,3]
print("Before updated lists", lists)
# add element in the via append methods at the end of the lists
lists.append(4)

print("After updated lists", lists)

# sort the lists in ascending order
lists.sort()
print("Sorted lists ascending ", lists)

# sort in the descending order

lists.sort(reverse = True)
print("Sorted lists in descending order",lists)

# Sorting methods apply on the character as well
fruits = ["banana", "apple", "litchi", "mango", "orange", "jaqfruit"]
fruits.sort()
print("Fruits in ascending sorted order ", fruits)
fruits.sort(reverse=True)
print("Fruits in descending sorted order ", fruits)

fruits.reverse()
print("Fruits in ascending sorted order ", fruits)

#lists insert methods
lists = [2,1,3]
print("lists in ascending order",lists)
lists.insert(1, 4)
print("After inserting at specific index updated lists",lists)

#lists remove or pop methods
lists.pop(1)
print("after removing element via pop methods ",lists)

# Lists extend methods
lists1 = [2,1,3,4]
lists2 = [1,2,3,4,5]
print("lists1 ", lists1)
print("lists2 ", lists2)
# extend the lists1
lists1.extend(lists2)
print("updated lists1 is ", lists1)
lists2.sort(reverse = True)
print("Reverse sorted lists2 is ", lists2)
#delete method
del lists2[0]
print("after Deleted 1st element from the lists2 ", lists2)
#insert at index 
lists2.insert(0, 5)
print("inderted element at index 0 updated lists is ", lists2)
#remove method remove element from lists
lists2.remove(1)
print("Updated lists2 after removing elements from lists ",lists2)

# clear methods clear and empty lists
lists1 = [2,1,3]
print("lists1 is: ", lists1)
lists1.clear()
print("After clearing lists: ", lists1)






