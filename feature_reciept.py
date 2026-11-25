class Receipt:
    def __init__(self, items, price, quantity, total_amount):
        self.items = items
        self.price = price
        self.quantity = quantity
        self.total_amount = total_amount

    def display_receipt(self):
        print("Receipt:")
        for item, price, quantity in zip(self.items, self.price, self.quantity):
            print(f"{item}: {quantity} x ${price:.1f}")
        print(f"Total Amount: ${self.total_amount:.1f}")

    def items(self):
        items = [item for item in self.items]
        return items

Burger = 1
Fries = 2
Soda = 3

user_input = input("Enter product number(1-3) ")
if user_input == "1":
    items = ["Burger"]
    prices = [5.99]
    quantities = [int(input("Enter quantity: "))]
elif user_input == "2":
    items = ["Fries"]
    prices = [2.99]
    quantities = [int(input("Enter quantity: "))]
elif user_input == "3":
    items = ["Soda"]
    prices = [1.99]
    quantities = [int(input("Enter quantity: "))]

prices = [5.99, 2.99, 1.99]
quantities = []
total_amount = sum(price * quantity for price, quantity in zip(prices, quantities))
receipt = Receipt(prices, quantities, total_amount)

receipt = f

