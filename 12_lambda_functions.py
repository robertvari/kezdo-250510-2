add_numbers = lambda a, b : a+b
divide_numbers = lambda a,b: a/b
multiply_numbers = lambda a,b: a*b

add_result = add_numbers(20, 10)
divide_result = divide_numbers(10, add_result)
multiply_result = multiply_numbers(10, divide_result)

print(multiply_result)