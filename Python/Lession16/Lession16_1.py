# problems on various data structures

# problem 1: List
fruits = ["apple","banana","cherry"]

print(fruits[0])  # Output: apple
fruits[1] = "orange"  # This will modify the list
print("after modifying the lists", fruits)
print("length of thelists is:", len(fruits))  # Output: 3

# problem 2: Lists

numbers = [x for x in range(1, 11)]  # List comprehension to create a list of numbers from 1 to 10
print("List of numbers from 1 to 10:", numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print first three elements and last three elements of the list
print("First three elements:", numbers[:3])  # Output: [1, 2, 3]
print("Last three elements:", numbers[7:])  # Output: [8, 9, 10]

#problem 3: List methods
numbers = [5,2,9,1,7]
print("Original list:", numbers)
numbers.sort()
print("Sorted list numbers:", numbers)  # Output: [1, 2, 5, 7, 9]
numbers.append(10)  # Adding an element to the end of the list
print("List after appending 10:", numbers)  # Output: [1, 2, 5, 7, 9, 10]
numbers.remove(2)  # Removing an element from the list
print("List after removing 2:", numbers)  # Output: [1, 5, 7, 9, 10]

names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")  # Inserting an element at index 1
print("List after inserting David at index 1:", names)  # Output: ['Alice', 'David', 'Bob', 'Charlie']

#problem 4: sets
my_set = {1, 2, 3, 3, 4}
print("Original set:", my_set)  # Output: {1, 2, 3, 4} (duplicates are removed  )

my_set.add(5)  # Adding an element to the set
print("Set after adding 5:", my_set)  # Output: {1, 2, 3, 4, 5}

my_set.remove(4)  # Removing an element from the set
print("Set after removing 4:", my_set)

#check weather 4 is present in the set or not
if 4 in my_set:
    print("4 is present in the set")
else:
    print("4 is not present in the set")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union_ele = a.union(b) # Find the union of sets a and b
print("Union of sets a and b:", union_ele)

intersection_ele = a.intersection(b) # Find the intersection of sets a and b
print("Intersection of sets a and b:", intersection_ele)

difference_ele = a.difference(b)    # Find the difference of sets a and b
print("Difference of sets a and b:", difference_ele)
    
#problem 5: Tuples
coordinates = (10, 20)
print("Coordinates:", coordinates)  # Output: (10, 20)

# coordinates[0] = 15  # This will raise an error because tuples are immutable

my_list = list(coordinates) # this will convert the tuple into a list
print("converted tuples into the lists:", my_list)

my_list[0] = 50     # Now we can modify the list
tuple = tuple(my_list)  # Convert the list back to a tuple
print("Modified tuple:", tuple)  # Output: (50, 20)

#problem 6: Dictionaries
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "grade": "A",
    "city": "New York"
}

print("Student dictionary:", student)  # Output: {'name': 'John', 'age': 20, 'major': 'Computer Science', 'grade': 'A', 'city': 'New York'}
print("Student name:", student["name"])  # Output: John
print("Student age:", student["age"])  # Output: 20
print("Student major:", student["major"])  # Output: Computer Science
print("Student grade:", student["grade"])  # Output: A
print("Student city:", student["city"])  # Output: New York

friends = {
    "kaushik": 8849835737,
    "Heena": 8160707158,
    "hetansh": 7342073420,
    
}
print("All keys in the friends dictionary:", friends.keys())  # Output: dict_keys(['name', 'number'])
print("All values in the friends dictionary:", friends.values())  # Output: dict_values(['Heena', 8849835737])
print("All items in the friends dictionary:", friends.items())  # Output: dict_items([('name', 'Heena'), ('number', 8849835737 )])

#print key and value of the dictionary using for loop
for key, value in friends.items():
    print(f"Friend: {key}, Phone Number: {value}")


#take numbers from the user and store them in a list until the user enters 'done'. Then print the list of numbers.
numbers = []
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)  # Convert input to integer
        numbers.append(number)  # Add the number to the list
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done' to finish.")

print(" oriiginal List of numbers:", numbers)
numbers_set = set(numbers)  # Convert the list to a set to remove duplicates
print("List of unique numbers:", list(numbers_set))

# Find product with higher prices
products = {
    "oil": 100,
    "sugar": 50,
    "rice": 80,
    "flour": 60,
    "salt": 30,
    "soda": 40,
    "cheeze": 120,
}

highest_price_product = max(products, key=products.get)  # Find the product with the highest price
print("Product with the highest price:", highest_price_product, "with price:", products[highest_price_product])  # Output: Product with the highest price: cheeze with price: 120

#create 2 dictionaries and merge them into a single dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print("Dictionary 1:", dict1)  # Output: Dictionary 1: {'a': 1, 'b': 2}
print("Dictionary 2:", dict2)  # Output: Dictionary 2: {'c': 3, 'd': 4}
merged_dict = dict1 | dict2  # Merge the two dictionaries
# merged_dict = {**dict1, **dict2}  # Another way to merge dictionaries
print("Merged dictionary:", merged_dict)  # Output: Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

