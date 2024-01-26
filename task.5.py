units = int(input("enter any unit:"))
if(units>0 and units<100):
    payamount=units*1.50
elif(units>=100 and units<200):
    payamount=units*2.50
elif(units>=200 and units<300):
    payamount=units*3.50

print("payamount:",payamount)

