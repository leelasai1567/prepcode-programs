amount = float(input("Enter total shopping amount:"))
if amount >= 1000:
    discount = amount * 10 / 100
    final_amount = amount - discount
    print("Discount = ", discount)
    print("Final amount = ", final_amount)
else:
    discount = 0
    final_amount = amount
    print("No discount")
    print("Final amount = ", final_amount)
    