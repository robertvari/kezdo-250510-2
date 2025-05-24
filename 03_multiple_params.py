import random, time

# define a function
def coffee_maker(coffee_type, water, beans):
    if water and beans:
        print(f"Making a {coffee_type}...")
        time.sleep(random.randint(1, 4))
        print(f"Your {coffee_type} is ready :)")
    else:
        if not water:
            print("Fill up the water tank.")
        if not beans:
            print("Fill up beans.")


coffee_maker("Latte", True, True)