#Sample program to understand for loop with break and continue statements in Python

# Example 1: Using break statement
print("Example 1: Using break and continue statement")

i = 20

for i in range(1,i+1):
    if i == 10:
        print("Breaking the loop at i =", i)
        break
    elif i == 5:
        print("Continuing the loop at i =", i)
        continue
    print("Current value of i:", i)
print("Loop ended.")
