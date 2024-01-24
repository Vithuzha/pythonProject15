cost_price=float(input("enter cost price"))
selling_price=float(input("enter selling price"))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("profit")
elif cost_price>selling_price:
    loss=cost_price-selling_price
    print("loss")
else:
    print("no profit no loss")
