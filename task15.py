amount = int(input("enter any sale amount"))
if amount >= 5000:
    discount = amount*0.15
elif amount < 5000:
    discount = amount*0.10

print("discount:",discount)
print("net pay :",amount-discount)



