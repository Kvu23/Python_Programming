
#this functions provides Additions of 2 numbers
def addition(a,b):
    return a+b

#this functions provides Substractions of 2 numbers
def substraction(a,b):
    return a-b
#this functions provides Multiplications of 2 numbers
def multiplication(a,b):
    return a*b
#this functions provides division of 2 numbers
def division(a,b):
    if b == 0:
        print("\nDivision by zero not possible")
        return None
    else:
        return a/b