import random, time


# define a function
def coffee_maker(coffee_type: str, water: bool, beans: bool):
    coffee_types = ["Espresso", "Doppio", "Latte", "Cappuccino"]

    if water and beans and coffee_type in coffee_types:
        print(f"Making a {coffee_type}...")
        time.sleep(random.randint(1, 4))
        print(f"Your {coffee_type} is ready :)")
    else:
        if not water:
            print("Fill up the water tank.")
        if not beans:
            print("Fill up beans.")
        if not coffee_type in coffee_types:
            print(f"{coffee_type} is not in my program.")
            print(f"I can make these types of coffee: {coffee_types}")

coffee_maker("Latte", True, True)