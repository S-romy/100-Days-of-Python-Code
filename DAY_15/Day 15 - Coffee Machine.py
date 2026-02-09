MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}

profit = 0


def user_interface(dict_input):
    """Shows the values of the resources dictionary."""
    print(f"Water: {dict_input['water']}ml")
    print(f"Milk: {dict_input['milk']}ml")
    print(f"Coffee: {dict_input['coffee']}g")


def enough_resources(resources_available, ingredients):
    """Determines if the resources are sufficient to make the coffee."""
    for item in ingredients:
        if resources_available[item] < ingredients[item]:
            return f"Sorry. Not enough {item}!"
    else:
        return "Please insert coins."


def make_coffee(resource_available, ingredients):
    """If resources are enough then the coffee is made."""
    for items in ingredients:
        resource_available[items] -= ingredients[items]
    return resource_available


def calc_coins():
    """Calculates the total amount of money deposited."""
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def is_transaction_successful(amount, cost):
    """Outlines the conditions the coffee machine should follow when it comes to money."""
    global profit
    if amount > cost:
        change = amount - cost
        profit += cost
        return f"Here is your change: ${round(change, 2)}"
    elif amount == cost:
        profit += cost
        return "Payment received successfully!"
    else:
        return f"Not enough money. ${round(amount, 2)} refunded!"


def coffee_machine():
    """The Coffee machine function that calls the other functions and decide how they operate."""
    global profit
    is_on = True
    while is_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            user_interface(resources)
            print(f"Money: ${profit}")
            is_on = True
        elif user_input in MENU:
            drink = MENU[user_input]
            result = enough_resources(resources, drink["ingredients"])
            print(result)

            if result == "Please insert coins.":
                user_money = calc_coins()
                drink_price = MENU[user_input]["cost"]
                print(is_transaction_successful(user_money, drink_price))

                make_coffee(resources, drink["ingredients"])
                print(f"Here is your {user_input} ☕. Enjoy!")

        elif user_input == "off":
            is_on = False


coffee_machine()
