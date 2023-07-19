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
    "money": 0,
}


def coffee_machine():
    proceed_function = True
    decision = input("what would you like? (1.espresso/2.latte/3.cappuccino): ")
    if decision == "off":
        return decision
    elif decision == "report":
        report(resources)
        return
    elif decision in ["espresso", "latte", "cappuccino"]:
        sufficient = check_resources(MENU.get(decision))
        if sufficient != True:
            print(sufficient)
            return
        coins = {
            "quarters": 0,
            "dimes": 0,
            "nickles": 0,
            "pennies": 0,
        }
        coin_sum = coin_process(coins)
        charge = transaction_process(coin_sum, MENU[decision])
        if charge < 0:
            print("Sorry that's not enough money. Money refunded")
            return
        elif charge > 0:
            print("“Here is $" + str(charge) + " dollars in change.")
        print (resources['money'])
        coffee_process (MENU[decision])

# TODO: 1. print report
def report(resource):
    for key, value in resource.items():
        print(key, ": ", value, sep='')


# TODO: 2. Check resource sufficient
def check_resources(coffee):
    sufficient = True
    # print(coffee.get("ingredients"))
    ingredients = coffee.get("ingredients")
    # print(resources)
    for key, value in resources.items():
        if key in ingredients:
            if value < ingredients.get(key):
                sufficient = "sorry, there is not enough " + key
    return sufficient


#: TODO 3. process coins

def coin_process(coins):
    for key, value in coins.items():
        coins[key] = int(input(key + ":"))
    coin_sum = 0.25 * coins["quarters"] + 0.10 * coins["dimes"] + 0.05 * coins["nickles"] + 0.01 * coins["pennies"]
    print("Coin sum is: ", coin_sum)
    return coin_sum


# TODO 4. Check transaction
def transaction_process(coins, coffee):
    global resources
    price = coffee["cost"]
    charge = coins - price
    if charge >= 0:
        resources['money'] += price
    return charge





# TODO 5. make coffee
def coffee_process (coffee):
    global resources
    ingredients = coffee['ingredients']
    print (ingredients)
    print (resources)
    for key, value in ingredients.items():
        resources[key] -= ingredients[key]
    return

choose = None
while choose != "off":
    choose = coffee_machine()
