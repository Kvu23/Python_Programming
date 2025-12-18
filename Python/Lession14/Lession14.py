#this is sample code for Lession14 which explains loop control statements in Python
# this example program demonstrates for  loop programming in Python

number = int(input("Enter a number to print its multiplication table: "))

print("\nUsing for loop to print multiplication table:")
for i in range(1, 11):
    print(number, "x", i, "=", i * number)
    
# same example using while loop
print("\nUsing while loop to print multiplication table:")

i = 1
while i <= 10:
    print(number, "x", i, "=", i * number)
    i += 1

