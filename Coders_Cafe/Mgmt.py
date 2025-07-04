def calculate_bill():
    global Bill
    
    while True:
        item = input("Enter the item you want to order (or type done to finish): ").strip().title()
        if item.lower()== 'done':
               # Generating the BILL;
            print("\n\033[1m---- Your Order Summary ----\033[0m")
            print(f"\033[1mCustomer Name: {name}\033[0m")
            for i, (item, qty, total) in enumerate(orders, 1):
                print(f"{i}. {item} X {qty} = Rs. {total}")
            print("\nThank you for your order\n Your Total Bill is: Rs.", Bill, "/-")
            break
        if item in menu:
            quantity = int(input(f"How many {item}'s would you like to order? "))
            item_total = menu[item] * quantity
            Bill += item_total
            print(f"{quantity} {item}'s added to your order.\n Item_Total: Rs. {item_total}/- | Current_Bill is: Rs. {Bill}/-")
        else:
            print(f"Sorry '{item}' is not on the menu. Please choose from the availlable items.")

        orders.append((item, quantity, item_total))

# Defining the menu of the Restruant mgmt. system

menu = {
    'Pizza':60,
    'Burger':50,
    'Pasta':70,
    'Salad':30,
    'Soda':20,
    'Water':10,
    'Coffee':25,
}

name = input("Enter your name: ").strip().title()
print("Welcome to the Coder's Cafe")
print("Here is the menu:\n")
print("\033[1mItem\tPrice\033[0m")   # Using ANSI escape codes for bold text
for item, price in menu.items():
    print(f"{item}\tRs. {price}/-")

Bill = 0
orders = []  # List to store orders

calculate_bill()  # This calls the function

