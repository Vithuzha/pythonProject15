side1=int(input("enter side1 value"))
side2=int(input("enter side2 value"))
side3=int(input("enter side3 value"))
if side1==side2==side3:
    print("Equilateral triangle")
elif side1!=side2!=side3:
    print("scalene triangle")
else:
    print("Isosceles triangle")
