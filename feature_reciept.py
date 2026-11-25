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
