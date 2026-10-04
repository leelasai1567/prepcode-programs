price=int(input("enter the price"))
discount=int(input("enter the discount"))

discount_amount=(discount/100)*price

print(F" discount_amount :{discount_amount}")
print(F"total _price:{price-discount_amount}")