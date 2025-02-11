def midpoint(begin_point, end_point):
    print('test', begin_point, end_point)
    return (begin_point + end_point)/2

def squareroot (number):
    return number**0.5

def exponent(base, exp):
    """Returns base raised to the power of exp."""
    return base ** exp  

def min_value(num1, num2):
    """Returns the minimum of two numbers."""
    return num1 if num1 < num2 else num2 

def max_value(num1, num2):
    """Returns the maximum of two numbers."""
    return (num1 > num2)*num1 + (num1<= num2)* num2

#Extra Credit: take two numbers x,y, 

def apply_function (x, y, func):
    return f"The function {func.__name__}({x}, {x}) = {func(x,y)}"