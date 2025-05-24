import random, time

# define a function
def coffee_maker():
    print("Making a coffee...")
    time.sleep(random.randint(1, 4))
    print("Your coffee is ready :)")


# call a function
coffee_maker()