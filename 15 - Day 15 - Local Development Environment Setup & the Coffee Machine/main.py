MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report(resource: dict):
    """
    prints information about the resources available

    Args:
        resource: dictionary with information about the resources available

    Returns: prints information about the resources available

    """
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(choice: str):
    """
    Checks if the resource is sufficient.
    Args:
        choice: user choice

    Returns: returns true if resource is sufficient
            or the resource that is deficient

    """
    choice_requirements = MENU[choice]["ingredients"]
    for item in choice_requirements:
        if choice_requirements[item] > resources[item]:
            print("Sorry you don't have enough " + item)
            return False
    return True


def process_coins(choice: str):
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nicks: "))
    pennies = int(input("How many pennies: "))
    paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    cost = MENU[choice]["cost"]
    global profit
    if paid >= cost:
        profit += paid
        if paid > cost:
            change = profit - cost
            print(f"Here is ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded!!")
        return False


profit = 0

is_working = True
while is_working:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_choice == "off":
        is_working = False

    elif coffee_choice == "report":
        report(resources)

    else:
        if is_resource_sufficient(coffee_choice):
            if process_coins(coffee_choice):
                choice_ingredients = MENU[coffee_choice]["ingredients"]
                for ingredient in choice_ingredients:
                    resources[ingredient] -= choice_ingredients[ingredient]
                print(f"Here is your {coffee_choice} ☕. Enjoy!")
