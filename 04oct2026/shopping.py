notebook_price = float(input(" enter the amount of notebook"))
pen_price=int(input("enter the amount of pen"))

notebook_quantity =int(input("enter the quantity of notebook"))
pen_quantity = int(input("enter the  pen quantity"))

notebook_total = notebook_price * notebook_quantity
pen_total = pen_price * pen_quantity

total_bill = notebook_total + pen_total

print("Notebook total =", notebook_total)
print("Pen total =", pen_total)
print("Total bill =", total_bill)