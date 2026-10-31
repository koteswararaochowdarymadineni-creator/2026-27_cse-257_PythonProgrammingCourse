
# Retail Billing with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

items = []

for i in range(n):
    print("\nEnter details of Product", i + 1)

    name = input("Product Name: ")
    category = input("Category (electronics/clothing/grocery/other): ").lower()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    amount = price * quantity

    # Category-specific tax
    if category == "electronics":
        tax_rate = 18
    elif category == "clothing":
        tax_rate = 5
    elif category == "grocery":
        tax_rate = 0
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    items.append([name, quantity, price, amount, tax])

# Calculate total before discount
total = subtotal + total_tax

# Apply threshold discount
if subtotal > 5000:
    discount_rate = 10
elif subtotal > 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
if discount > 1000:
    discount = 1000

# Final bill
final_amount = total - discount

# Display invoice
print("\n========== RETAIL INVOICE ==========")

print("\nProduct\tQty\tPrice\tAmount\tTax")

for item in items:
    print(item[0], "\t", item[1], "\t",
          item[2], "\t", item[3], "\t", item[4])

print("------------------------------------")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Discount       : Rs.", round(discount, 2))
print("Final Amount   : Rs.", round(final_amount, 2))

print("====================================")
print("Thank you for shopping!")

