from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

items = menu.get_items()
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        # Turn OFF
        is_on = False
    elif choice == "report":
        # secret report
        coffee_maker.report()
    elif choice in items:
        print(f"You selected {choice}")
        # Assign a MenuItem instance
        drink = menu.find_drink(choice)
        # Check if resources is sufficient and user inputs enough money
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Deduct the ingredients used for coffee
            coffee_maker.make_coffee(drink)
    else:
        print("Invalid Selection")
