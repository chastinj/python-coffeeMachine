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
#TODO Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def prompt():
    '''give question to the user to start the coffee making process '''
    return input(f"What would you like? (espresso/ latte / cappuccino): ").lower()

#TODO Turn off the Coffee Machine by entering “ off ” to the prompt.
'''wile loop will stop once machine is on is false'''
machine_is_on = True

#TODO Print report.
def report():
    '''gives a report if response is "report" '''
    earnings = resources["money"]
    print(f'Water: {resources["water"]} , Milk: {resources["milk"]}, Coffee: {resources["coffee"]}, '
          f'Money:' + "${:.2f}".format(earnings))

#TODO Check resources sufficient?
def check_sufficiency(drink):
    '''make sure we have enough resources '''
    is_enough = False
    this_water = MENU.get(drink).get("ingredients").get("water")
    if "milk" not in MENU.get(drink).get("ingredients").keys():
        this_milk = 0
    else:
        this_milk = MENU.get(drink).get("ingredients").get("milk")
    this_coffee = MENU.get(drink).get("ingredients").get("coffee")

    resource_water = resources.get("water")
    resource_milk = resources.get("milk")
    resources_coffee = resources.get("coffee")

    milk_level = resource_milk - this_milk
    water_level = resource_water - this_water
    coffee_level = resources_coffee - this_coffee

    got_milk = milk_level > 0
    got_water = water_level > 0
    got_coffee = coffee_level > 0

    if not got_coffee:
        print(f"sorry, not enough coffee!")
    elif not got_water:
        print(f"sorry not enough water!")
    elif not got_milk:
        print(f"Sorry, not enough milk!")
    else:
        is_enough = True

    return is_enough





#TODO Process coins
def process_coins(quarter=0,dime=0, nickle=0, penny=0, drink =" "):
    total = 0
    pour_drink = False
    qt = quarter * 0.25
    d = dime * 0.10
    nic = nickle * 0.05
    pen = penny * 0.01

    total = qt + d + nic + pen
    print("amount given:" + "${:.2f}".format(total))
    print("amount needed:" + "${:.2f}".format(MENU.get(drink).get("cost")))

    if total == MENU.get(drink).get("cost"):
        pour_drink = True
        resources["money"] += total
    else:
        print("Insufficient funds")

    return pour_drink



#TODO Check transaction successful

#TODO Make Coffee
def make_coffee(drink):
    this_water = MENU.get(drink).get("ingredients").get("water")
    if "milk" not in MENU.get(drink).get("ingredients").keys():
        this_milk = 0
    else:
        this_milk = MENU.get(drink).get("ingredients").get("milk")
    this_coffee = MENU.get(drink).get("ingredients").get("coffee")

    resource_water = resources.get("water")
    resource_milk = resources.get("milk")
    resources_coffee = resources.get("coffee")

    milk_level = resource_milk - this_milk
    water_level = resource_water - this_water
    coffee_level = resources_coffee - this_coffee

    resources["water"] = water_level
    resources["milk"] = milk_level
    resources["coffee"] = coffee_level
    print(f" \“Here is your {drink}. Enjoy!\”.")


if __name__ == "__main__":
    while machine_is_on:
        request = prompt()
        if (request == "off"):
            machine_is_on = False
            break
        elif (request == "report"):
            report()
        elif (request == "espresso" or request =="latte" or request=="cappuccino"):
            if (check_sufficiency(request) == True):
                cost_to_pay = MENU.get(request).get("cost")
                funds = input("Please insert "+"${:.2f}".format(cost_to_pay)
                              + " in each coin type amount separated by a comma (quarters , dimes, nickels, pennies):")
                list_of_coins = []
                list_of_coins = funds.split(",")
                #print(list_of_coins)
                make_drink = process_coins(int(list_of_coins[0]),int(list_of_coins[1]),int(list_of_coins[2]),int(list_of_coins[3]), request)
                if make_drink:
                    make_coffee(request)
            else:
                print(f"There is not enough resources! Sorry. Make a different choice.")




