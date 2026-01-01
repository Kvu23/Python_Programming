# Define a variable
name = "John"
print(f"Variable defined: {name}")

# Delete the variable
del name

# Trying to access deleted variable will raise NameError
try:
    print(name)
except NameError:
    print("Variable has been deleted and no longer exists")