import random, time

# define a function
def coffee_maker(coffee_type):
    print(f"Making a {coffee_type}...")
    time.sleep(random.randint(1, 4))
    print(f"Your {coffee_type} is ready :)")


coffee_maker("Doppio")
coffee_maker("Americano")
coffee_maker("Latte")