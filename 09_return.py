def add_numbers(a, b):
    return a+b

def divide_numbers(a, b):
    return a/b

def multiply_numbers(a, b):
    return a*b

add_result = add_numbers(20, 10)
divide_result = divide_numbers(10, add_result)
multiply_result = multiply_numbers(10, divide_result)

print(multiply_result)