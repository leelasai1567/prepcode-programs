buying_price=int(input("enter the  amount of buying price"))
selling_price=int(input("enter the amount of  selling price"))
total_price=int(input("enter the  amount of total price"))
storage_price=int(input("enter the amount of storage price "))


profit=((selling_price-buying_price)* total_price)-storage_price
print(f"total profit:{profit}")