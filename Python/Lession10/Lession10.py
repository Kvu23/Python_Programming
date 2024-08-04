# Tuple
tup = (2,1,3)
print(type(tup))
# print individual elements same as strings
print(tup[0])
print(tup[1])
print(tup[2])
# tup[2] = 2   tuple are immutable objects not allowed

#create an empty tuple
tup = ()
print(tup)
print("type of empty tuple", type(tup))
# only 1 element tuple
tup = (1, )
print(tup)
print("type of tuple", type(tup))

# slicing is same as lists in tuple
tup = (2,1,3,4,5,2)
print(tup)
print("slicing in tuple", tup[1:3])

#indexing in tuple
print("return index for 1st occurance of value ",tup.index(4))
#count method in tuple
print("Number of occurance is",tup.count(2))
