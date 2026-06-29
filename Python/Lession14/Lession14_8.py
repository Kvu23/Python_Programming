#Problem 1: Print numbers using for loop
# for i in range(1,11):
#     print("Number is:", i)

# Problem 2: Print even numbers using for loop    
# number = int(input("Enter a number: "))
# print("You entered:", number)

#Problem 3: Print multiplication table of a number using for loop
# for i in range(1, 11):
#     print(f'{number} x {i} = {number * i}')

#Problem 4: Print sum of first 100 numbers using for loop
# sum = 0
# for i in range(1, 101):
#     sum += i
# print("Sum of first 100 numbers is:", sum)

#Problem 5: Print a pattern using for loop
# for i in range(1, 6):
#     print("*"*i)
# for i in range(4, 0, -1):
#     print("*"*i) 

#Problem 6: Password guess using while loop
# password = "secret"
# guess = ""
# while guess != password:
#     guess = input("Enter password: ")
# print("Password correct!")


# # reverse a number using while loop
# num = int(input("Enter a number: "))
# print("You entered:", num)
# print("Reverse number is:", int((str(num))[::-1]))  # This line reverses the number again to show the original number

# rev_num = 0
# while num > 0:
#     digit = num % 10
#     rev_num = rev_num * 10 + digit
#     num = num // 10
    
# print("Reversed number using while loop is:", rev_num)

#Problem 7: Demonstrate break, continue, and pass statements in a for loop
for i in range(1, 11):
    if i == 7:
        print("breaking the loop at :", i)
        break
    elif i == 5:
        print("Skipping the loop at:", i)
        continue
    elif i == 3:
        print("passing the loop at:", i)
        pass
    else:
        print("Number is:", i)

