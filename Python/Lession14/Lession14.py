#this is sample code for Lession14 which explains loop control statements in Python
# this example program demonstrates for  loop programming in Python

number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", i * number)
    