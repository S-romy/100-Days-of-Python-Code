from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_machine = True
while coffee_machine:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ").lower()
    if user_input == "off":
        coffee_machine = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                profit = drink.cost
                if money_machine.make_payment(profit):
                    coffee_maker.make_coffee(drink)
