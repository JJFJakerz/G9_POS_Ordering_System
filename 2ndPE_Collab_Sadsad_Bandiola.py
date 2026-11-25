print("===== WELCOME MINI STORE POS ORDERING SYSTEM =====")

print("--- Product Menu ---")
print("1. Burger - PHP 50.00")
print("2. Fries - PHP 35.00")
print("3. Soft Drink - PHP 25.00")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

Product1 = Product("Burger", 50.00)
Product2 = Product("Fries", 35.00)
Product3 = Product("Soft Drink", 25.00)

# Store selected items in a list so we can easily print the receipt later
cart = []

# --- ITEM 1 ---
ProductNumber1 = input("\nEnter a Product Number (1-3): ")
Quantity1 = int(input("Enter Quantity: "))

if ProductNumber1 == "1":
    cart.append((Product1, Quantity1))
    print(f"Added: {Product1.name} x {Quantity1}")
elif ProductNumber1 == "2":
    cart.append((Product2, Quantity1))
    print(f"Added: {Product2.name} x {Quantity1}")
elif ProductNumber1 == "3":
    cart.append((Product3, Quantity1))
    print(f"Added: {Product3.name} x {Quantity1}")

# --- ITEM 2 ---
continue_ordering = input("\nDo you want to add another product? (yes/no): ")
if continue_ordering.lower() == "yes":
    ProductNumber2 = input("Enter a Product Number (1-3): ")
    Quantity2 = int(input("Enter Quantity: "))

    if ProductNumber2 == "1":
        cart.append((Product1, Quantity2))
        print(f"Added: {Product1.name} x {Quantity2}")
    elif ProductNumber2 == "2":
        cart.append((Product2, Quantity2))
        print(f"Added: {Product2.name} x {Quantity2}")
    elif ProductNumber2 == "3":
        cart.append((Product3, Quantity2))
        print(f"Added: {Product3.name} x {Quantity2}")

    # --- ITEM 3 (Only asks if they ordered Item 2) ---
    continue_ordering = input("\nDo you want to add another product? (yes/no): ")
    if continue_ordering.lower() == "yes":
        ProductNumber3 = input("Enter a Product Number (1-3): ")
        Quantity3 = int(input("Enter Quantity: "))

        if ProductNumber3 == "1":
            cart.append((Product1, Quantity3))
            print(f"Added: {Product1.name} x {Quantity3}")
        elif ProductNumber3 == "2":
            cart.append((Product2, Quantity3))
            print(f"Added: {Product2.name} x {Quantity3}")
        elif ProductNumber3 == "3":
            cart.append((Product3, Quantity3))
            print(f"Added: {Product3.name} x {Quantity3}")

# --- RECEIPT ---
print("\nYou may proceed to get the receipt.")
print("\n========== RECEIPT MINI STORE ==========")
print(f"{'Product':<12} {'Qty':<6} {'Price':<8} {'Subtotal'}")
print("-" * 40)

total = 0
for product, qty in cart:
    subtotal = product.price * qty
    total += subtotal
    print(f"{product.name:<12} {qty:<6} {product.price:<8.2f} {subtotal:.2f}")

print("-" * 40)
print(f"TOTAL AMOUNT: PHP {total:.2f}")
