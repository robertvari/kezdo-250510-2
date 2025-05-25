def recursive_function(number):
    number += 1
    print(f"Number: {number}")

    if number == 10:
        return  # None
    
    recursive_function(number)

recursive_function(0)