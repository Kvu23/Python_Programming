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







