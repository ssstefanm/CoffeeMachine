# program requirements
# 1. Print report
# 2. Check resources sufficient
# 3. Process coins
# 4. Check if transaction successful
# 5. Make coffee
machine_on = True
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
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


def report():
    print(f"water: {resources["water"]}")
    print(f"milk: {resources["milk"]}")
    print(f"coffee: {resources["coffee"]}")


def add_coins():
    print("Please add funds for the coffee: ")
    coins_added = 0
    penny_added = float(input("How many pennies? ")) * coins["penny"]
    coins_added = coins_added + penny_added
    print(f"Amount so far: ${coins_added}")
    nickel_added = float(input("How many nickels? ")) * coins["nickel"]
    coins_added = coins_added + nickel_added
    print(f"Amount so far: ${coins_added}")
    dime_added = float(input("How many dimes? ")) * coins["dime"]
    coins_added = coins_added + dime_added
    print(f"Amount so far: ${coins_added}")
    quarter_added = float(input("How many quarters? ")) * coins["quarter"]
    coins_added = coins_added + quarter_added
    print(f"Amount so far: ${coins_added}")

    return coins_added


def espresso():
    coins_added = add_coins()
    if resources["water"] >= MENU['espresso']['ingredients']['water']:
        if resources["coffee"] >= MENU['espresso']['ingredients']['coffee']:
            if coins_added >= 1.5:
                resources["water"] = resources["water"] - MENU['espresso']['ingredients']['water']
                resources["coffee"] = resources["coffee"] - MENU['espresso']['ingredients']['coffee']
                change = coins_added - MENU["espresso"]["cost"]
                print(f"Here is your ${round(change, 2)} of change.")
                print("Enjoy your ☕Espresso!")
                return resources
            else:
                print("Sorry, not enough money added, please insert the necessary amount instead.")
                print(f"Your ${round(coins_added, 2)} have been returned")
        else:
            print("Sorry, there is not enough coffee in the machine. Try again later!")
    else:
        print("Sorry, there is not enough water in the machine. Try again later!")




def latte():
    coins_added = add_coins()
    if resources["water"] >= MENU['latte']['ingredients']['water']:
        if resources["coffee"] >= MENU['latte']['ingredients']['coffee']:
            if resources["milk"] >= MENU['latte']['ingredients']['milk']:
                if coins_added >= 2.5:
                    resources["water"] = resources["water"] - MENU['latte']['ingredients']['water']
                    resources["coffee"] = resources["coffee"] - MENU['latte']['ingredients']['coffee']
                    resources["milk"] = resources["milk"] - MENU['latte']['ingredients']['milk']
                    change = coins_added - MENU["latte"]["cost"]
                    print(f"Here is your ${round(change, 2)} of change.")
                    print("Enjoy your ☕Latte!")
                    return resources
                else:
                    print("Sorry, not enough money added, please insert the necessary amount instead.")
                    print(f"Your ${round(coins_added, 2)} have been returned")
            else:
                print("Sorry, there is not enough milk in the machine. Try again later!")
        else:
            print("Sorry, there is not enough coffee in the machine. Try again later!")
    else:
        print("Sorry, there is not enough water in the machine. Try again later!")




def cappuccino():
    coins_added = add_coins()
    if resources["water"] >= MENU['cappuccino']['ingredients']['water']:
        if resources["coffee"] >= MENU['cappuccino']['ingredients']['coffee']:
            if resources["milk"] >= MENU['cappuccino']['ingredients']['milk']:
                if coins_added >= 3.0:
                    resources["water"] = resources["water"] - MENU['cappuccino']['ingredients']['water']
                    resources["coffee"] = resources["coffee"] - MENU['cappuccino']['ingredients']['coffee']
                    resources["milk"] = resources["milk"] - MENU['cappuccino']['ingredients']['milk']
                    change = coins_added - MENU["espresso"]["cost"]
                    print(f"Here is your ${round(change, 2)} of change.")
                    print("Enjoy your ☕Cappuccino!")
                    return resources
                else:
                    print("Sorry, not enough money added, please insert the necessary amount instead.")
                    print(f"Your ${round(coins_added, 2)} have been returned")
            else:
                print("Sorry, there is not enough milk in the machine. Try again later!")
        else:
            print("Sorry, there is not enough coffee in the machine. Try again later!")
    else:
        print("Sorry, there is not enough water in the machine. Try again later!")




while machine_on:
    choice = input("What would you like? espresso/latte/cappuccino: ")

    if choice == "latte":
        latte()
    elif choice == "espresso":
        espresso()
    elif choice == "cappuccino":
        cappuccino()
    elif choice == "report":
        report()
    elif choice == "off":
        machine_on = False
