from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_machine = Menu()
drinks = menu_machine.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

isOn = True
while isOn:
    choice = input("What would you like?" + drinks + ": ")
    
    if choice  == "off":
        isOn = False
    elif choice  == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_chosen = menu_machine.find_drink(choice) 
        if coffee_maker.is_resource_sufficient(drink_chosen) and money_machine.make_payment(drink_chosen.cost):
            coffee_maker.make_coffee(drink_chosen)


