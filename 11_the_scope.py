# global scope
NAME = "Tamás"

def say_hello():
    # global NAME
    # local scope of say_hello
    # name = "csilla"
    NAME = "Csilla"
    print(NAME)

say_hello()
print(NAME)