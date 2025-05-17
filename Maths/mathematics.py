def summation(a, b):
    result = a + b
    return result

def subtraction(a, b):
    result = a - b
    return result

def multiplication(a, b):
    result = a * b
    return result

def division(a, b):
    if b != 0:
        result = a / b
    else:
        result = "Division by zero error"
    return result