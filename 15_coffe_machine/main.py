from menu import MENU
coffee_options = ["espresso", "latte","cappuccino"]

machine_state = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def print_report():
    print(f"Water: {machine_state['water']}ml")
    print(f"Milk: {machine_state['milk']}ml")
    print(f"Coffee: {machine_state['coffee']}g")
    print(f"Money:${machine_state['money']}")

def is_enough(ingredients):
    for ingredient in ingredients:
        if machine_state[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def update_machine_state(drink):
    for ingredient in drink["ingredients"]:
        machine_state[ingredient] -= ingredients[ingredient]
    machine_state["money"] += drink["cost"]

should_continue = True
while should_continue:
    chosen_item = input("What would you like? (espresso/latte/cappuccino): ")
    

    if chosen_item in coffee_options:
        drink = MENU[chosen_item]
        ingredients = drink["ingredients"]
        if is_enough(ingredients):
            print("Please insert coins.")
            quarters = float(input("How many quartes?:"))
            dimes = float(input("How many dimes?:"))
            nickles = float(input("How many nickles?:"))
            pennies = float(input("How many pennies?:"))
            total_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies
                                                                                 * 0.01) 
            change = total_money - drink["cost"]
            if change >= 0: 
                update_machine_state(drink)
                print(f"Here is ${change:.2f} in change")
                print(f"Here is your {chosen_item}. Enjoy!")
            else:
                print("Not Enough money, Money refunded")

    elif chosen_item == "report":
        print_report()

    elif  chosen_item == "off":
        should_continue = False

    else:
        print("It is not a valid choice")
