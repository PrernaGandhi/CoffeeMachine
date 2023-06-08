from data import resources
from data import MENU
from data import COINS_VALUE
from data import coffee_machine


def start_coffee_machine():
    """Start coffee machine"""
    print("Welcome to the Authentic Coffee Machine!! 🫘")
    coffee_machine.update(resources)
    profit = {
        "money": 0
    }
    coffee_machine.update(profit)
    return True
    # print(coffee_machine)


# TODO 2: Check if there are sufficient ingredients present for order
# TODO 3: Give user feedback if their order can't be completed if ingredients are not available
def are_ingredients_available(input_order):
    """Checks if ingredients are available for the user order"""
    ingredients_required = MENU[input_order]['ingredients']
    for ingredient in ingredients_required:
        if ingredient in coffee_machine:
            quantity_available = coffee_machine[ingredient]
            quantity_required = ingredients_required[ingredient]
            if quantity_available < quantity_required:
                print(f"Sorry your order can't be processed, there isn't enough {ingredient} 😞")
                return False
        else:
            return False
    return True


def get_user_amount():
    """Input user amount and calculate the total amount of coins inserted by the user"""
    # TODO 4: Ask user to insert coins for coffee entered
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))
    quarters_total = quarters * COINS_VALUE["quarters"]
    dimes_total = dimes * COINS_VALUE["dimes"]
    nickels_total = nickels * COINS_VALUE["nickels"]
    pennies_total = pennies * COINS_VALUE["pennies"]
    user_amount = round(quarters_total + dimes_total + nickels_total + pennies_total, 2)
    return user_amount


# TODO 5: Check if the amount entered is sufficient for the order
def calculate_difference(user_amount, user_order):
    """Calculate the difference between the amount inserted by the user and the order amount required"""
    order_value = MENU[user_order]["cost"]
    return user_amount - order_value


def process_change_or_refund(difference_amount):
    """Process change amount"""
    if difference_amount > 0:
        return f"Here is your change of ${difference_amount}"
    elif difference_amount == 0:
        return "The difference amount is 0"
    # print(f"{difference_amount}")
    return f"Sorry that's not enough money. Money refunded."


# TODO 6: Make coffee
def make_coffee(user_order):
    """Make Coffee"""
    # print(f"Before making coffee : {resources}")
    ingredients_required = MENU[user_order]["ingredients"]
    for ingredient in ingredients_required:
        coffee_machine[ingredient] -= ingredients_required[ingredient]
    # print(f"After making coffee : {resources}")
    return f"Enjoy your {user_order} ☕. Have a nice day!! ☺️"


def generate_report():
    """Generate report for number of resources left"""
    for item in coffee_machine:
        key = item.title()
        if item in resources:
            value = coffee_machine[item]
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: ${coffee_machine[item]}")


# TODO 7: Add cost of the drink as the profit to the coffee machine
def add_profit(user_order):
    """Add profit to the coffee machine"""
    profit = MENU[user_order]["cost"]
    coffee_machine["money"] += profit
    # print(coffee_machine)


def stop_coffee_machine():
    """Stop coffee machine"""
    print("Goodbye! Have a nice day!!! ☺️")
    return False


def lets_have_coffee():
    """Main function to operate coffee machine"""
    is_coffee_machine_on = start_coffee_machine()
    # TODO 1: Display the choice to user from (espresso/latte/cappuccino).
    while is_coffee_machine_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            generate_report()
        elif order in MENU:
            if are_ingredients_available(order):
                # if yes, ask user to enter coins
                total_amount = get_user_amount()
                difference = calculate_difference(total_amount, order)
                # TODO 8: Return change
                # TODO 9: or Return refund
                print(process_change_or_refund(difference))
                if difference >= 0:
                    print(make_coffee(order))
                    add_profit(order)
        elif order == "off":
            is_coffee_machine_on = stop_coffee_machine()
        else:
            print(f"Sorry I don't understand your choice")


lets_have_coffee()