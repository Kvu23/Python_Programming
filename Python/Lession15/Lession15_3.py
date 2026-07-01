# programs to understand fibonacci number using recursion
def fibonacci(n):
    '''Calculate the nth Fibonacci number using recursion.'''
    '''base case for 0 and 1'''
    
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci of 5 is:", fibonacci(5))

#program to find factorial of a number using recursion
def factorial(n):
    '''Calculate the factorial of a number using recursion.'''
    ''' return 1 for the base case if number is 0, otherwise return n multiplied by the factorial of n-1.'''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")




