num1=int(input("Enter side 1: "))
num2=int(input("Enter side 2: "))
num3=int(input("Enter side 3: "))

avg= (num1+num2+num3)/2 #semi perimeter
s=float(avg)
area = (s*(s-num1)*(s-num2)*(s-num3)) ** 0.5

print("Area of the triangle is:",area)
