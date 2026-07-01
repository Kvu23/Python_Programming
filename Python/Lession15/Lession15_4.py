# programs to understand modules in pythons.

#import the necessary modules first
import math
# import mymodule

print("The value of pi is:", math.pi)
print("The square root of 16 is:", math.sqrt(16))
print("The factorial of 5 is:", math.factorial(5))
print("The logarithm of 1000 to base 10 is:", math.log10(1000))
print("The sine of 30 degrees is:", math.sin(math.radians(30)))
print("The cosine of 45 degrees is:", math.cos(math.radians(45)))
print("The sum of products of (1, 2) and (3, 4) is:", math.fsum([1, 2]) * math.fsum([3, 4]))  # This line will raise an AttributeError since math module does not have a sumprod function.  

#function is calling from the mymodule.py file.
# mymodule.Hello()

import requests

response = requests.get("https://api.github.com")
print("status code is:", response.status_code)  # Output: 200
print("response is:", response.json(), sep='\n')  # Output: {'message': 'Not Found'}