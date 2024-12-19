def display_menu():
    """Displays the food menu with prices."""
    menu = {
        "burger": 80.00,
        "fries": 50.00,
        "spaghetti": 45.00,
        "1 piece chicken": 100.00,
        "soda": 35.00,
        "water": 15.00
    }
    print("\nWelcome to Macdollibee!!")
    print("Here's our Menu:\n")
    for item, price in menu.items():
        print(f"{item}: ₱{price:.2f}")
    return menu

def take_order(menu):
    """Allows the user to order multiple items."""
    order_items = {}
    print("\nEnter the items you want to order. Type 'done' to finish.")
    while True:
        order = input("Please enter a food item: ").strip()
        if order.lower() == 'done':
            break
        # Match input to menu keys, case insensitive
        matched_item = next((item for item in menu if item.lower() == order.lower()), None)
        if matched_item:
            quantity = input(f"How many {matched_item}(s) would you like? ")
            if quantity.isdigit():
                quantity = int(quantity)
                if matched_item in order_items:
                    order_items[matched_item] += quantity
                else:
                    order_items[matched_item] = quantity
                print(f"Added {quantity} {matched_item}(s) to your order.")
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Sorry, that's not on the menu. Please select a valid item.")
    return order_items

def calculate_total(order_items, menu):
    """Calculates the total cost of the order."""
    total_cost = sum(menu[item] * quantity for item, quantity in order_items.items())
    return total_cost

def display_order_summary(order_items, menu, total_cost):
    """Displays a summary of the user's order with itemized prices."""
    print("\nOrder Summary:")
    for item, quantity in order_items.items():
        print(f"{item} (x{quantity}): ₱{menu[item] * quantity:.2f}")
    print(f"\nTotal Cost: ₱{total_cost:.2f}")

def process_payment(total_cost):
    """Handles the payment process and ensures payment sufficiency."""
    while True:
        try:
            cash = float(input(f"\nThe total cost is ₱{total_cost:.2f}. Please enter your payment: ₱"))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Thank you for your purchase! Your change is: ₱{change:.2f}")
                break
            else:
                print(f"Insufficient payment! You need ₱{total_cost - cash:.2f} more.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    """Main function to run the food ordering system."""
    menu = display_menu()
    while True:
        order_items = take_order(menu)
        if not order_items:
            print("\nNo items were ordered. Exiting the system.")
            break
        total_cost = calculate_total(order_items, menu)
        display_order_summary(order_items, menu, total_cost)
        process_payment(total_cost)
        another_order = input("\nWould you like to place another order? (yes/no): ").strip().lower()
        if another_order != 'yes':
            print("\nThank you for dining at Macdollibee! Have a great day!")
            break

if __name__ == "__main__":
    main()
