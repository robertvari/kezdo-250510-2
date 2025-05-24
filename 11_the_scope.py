# global scope
NAME = "Tamás"

def say_hello():
    # local scope of say_hello
    name = "csilla"
    print(name, NAME)

say_hello()