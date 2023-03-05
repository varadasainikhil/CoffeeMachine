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


def check_resources(type_of_coffee):
    req_water = MENU[type_of_coffee]["ingredients"]["water"]
    req_coffee = MENU[type_of_coffee]["ingredients"]["coffee"]
    rem_water = resources["water"]
    rem_coffee = resources["coffee"]

    if type_of_coffee == 'latte' or type_of_coffee == 'cappuccino':
        req_milk = MENU[type_of_coffee]["ingredients"]["milk"]
        rem_milk = resources["milk"]
        if rem_milk < req_milk:
            print("Sorry, there is not enough milk.")
            return False
    if rem_water < req_water:
        print("Sorry, there is not enough water.")
        return False
    if rem_coffee < req_coffee:
        print("Sorry, there is not enough coffee powder.")
        return False
    else:
        return True


def calculate_change(type_of_coffee):
    no_of_quarters = int(input("Enter the number of quarters: "))
    no_of_dimes = int(input("Enter the number of dimes: "))
    no_of_nickels = int(input("Enter the number of nickles: "))
    no_of_pennies = int(input("Enter the number of pennies: "))
    total_given = round(no_of_quarters * 0.25 + no_of_dimes * 0.10 + no_of_nickels * 0.05 + no_of_pennies * 0.01, 2)
    cost = MENU[type_of_coffee]['cost']
    change = round(total_given - cost, 2)
    if change > 0:
        print(f"Cost of {type_of_coffee} is {cost}")
        print(f"Your change is {change}")
        return True
    else:
        print("Sorry that's not enough money. Money is refunded.")
        return False


def make_coffee(type_of_coffee):
    req_water = MENU[type_of_coffee]["ingredients"]["water"]
    req_coffee = MENU[type_of_coffee]["ingredients"]["coffee"]
    rem_water = resources["water"]
    rem_coffee = resources["coffee"]
    rem_water -= req_water
    rem_coffee -= req_coffee
    resources["water"] = rem_water
    resources["coffee"] = rem_coffee
    if type_of_coffee == 'latte' or type_of_coffee == 'cappuccino':
        req_milk = MENU[type_of_coffee]["ingredients"]["milk"]
        rem_milk = resources["milk"]
        rem_milk -= req_milk
        resources["milk"] = rem_milk
    print(f"Here is your {type_of_coffee}, enjoy it.")


def charge_for_coffee(type_of_coffee):
    resources["money"] += MENU[type_of_coffee]['cost']


def report():
    print(f"Remaining Milk : {resources['milk']}")
    print(f"Remaining Water : {resources['water']}")
    print(f"Remaining Coffee : {resources['coffee']}")
    print(f"Money : {resources['money']}")


def add(material):
    x = resources[material]
    x += 500
    resources[material] = x
    print(f"{material} added. New quantity of {material} is {x}")


serve = True
while serve:
    choice = input("What would you like ? (espresso/latte/cappuccino):")
    if choice.lower() == "end":
        serve = False
    elif choice.lower() == "espresso":
        if check_resources(choice) and calculate_change(choice):
            make_coffee(choice)
            charge_for_coffee(choice)
    elif choice.lower() == "latte":
        if check_resources(choice) and calculate_change(choice):
            make_coffee(choice)
            charge_for_coffee(choice)
    elif choice.lower() == "cappuccino":
        if check_resources(choice) and calculate_change(choice):
            make_coffee(choice)
            charge_for_coffee(choice)
    elif choice.lower() == "report":
        report()
    elif choice.lower() == "add water":
        add("water")
    elif choice.lower() == "add milk":
        add("milk")
    elif choice.lower() == "add coffee":
        add("coffee")
    else:
        print("Command not recognised.")