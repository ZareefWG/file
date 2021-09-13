Lenght = int(input("Enter the amount of Lenght: "))
Breadth = int(input("Enter the amound of Breadth: "))

area = Lenght*Breadth
perimeter = 2*(Lenght+Breadth)

if area > perimeter:
    print (area)
if area == perimeter:
    print ("equal")
    print (perimeter)
else:
    print (area)



Num1 = int(input("Enter Your Number: "))
Num2 = int(input("Enter Your Number: "))

if Num1 > Num2:
    print (Num1-Num2)
else:
    print (Num1 + Num2)
